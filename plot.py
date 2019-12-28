import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt

#import data as dt
import os








df=pd.read_csv("dati/df_fai.csv", sep=",")
df.columns=[i.lower() for i in df.columns]
df.columns=[i if "/" not in i else i.replace("/","-") for i in df.columns]
df.columns=[i if "€" not in i else i.replace("€","eur") for i in df.columns]
df.columns=[i if "%" not in i else i.replace("%","perc") for i in df.columns]



df.sort_values(by="abitanti",ascending=False)

df_abitanti=df.copy(deep=True)



mlt.rcParams["figure.figsize"]=(20,10)
mlt.rcParams["font.size"]=20


df_piccoli=df[df["abitanti"]<20000]

df_medi=df[df["abitanti"]<100000]
df_medi=df_medi[df_medi["abitanti"]>=20000]

df_grandi=df[df["abitanti"]<400000]
df_grandi=df_grandi[df_grandi["abitanti"]>=100000]

df_enormi=df[df["abitanti"]>=400000]
df_enormi=df_enormi[df_enormi["abitanti"]<1000000]

df_megalopoli=df[df["abitanti"]>=1000000]
df_megalopoli.iloc[:20]
df_megalopoli[df_megalopoli["anno"]==2019]






def migliori(df_local,folder):
    try:
        os.mkdir("../plots/"+folder)
    except OSError:
        pass

    dividendi=["tot_entrate","totale_n+r","ctb_visitatori"]
    targets=["luoghi_aperti","visitatori","abitanti","densità","reddito medio"]
    periodi=["GFP","GFA"]
    for dividendo in dividendi:
        try:
            os.mkdir("../plots/"+folder+"/"+dividendo)
        except OSError:
            pass
        for periodo in periodi:
            try:
                os.mkdir("../plots/"+folder+"/"+dividendo+"/"+periodo)
            except OSError:
                pass
            for target in targets:
                for anno in np.unique(df_local["anno"].to_numpy()):
                    fig=plt.figure()
                    df_primavera=df_local[df_local["tipo"]==periodo]
                    df_primavera=df_primavera[df_primavera["anno"]==anno]
                    df_primavera["target"]=df_primavera[dividendo]/df_primavera[target]
                    df_primavera.sort_values(by="target",ascending=False,inplace=True)
                    df_primavera=df_primavera.iloc[:20]
                    plt.bar((df_primavera['delegazione'].values).astype(str),df_primavera["target"])
                    plt.title(target+"  "+str(anno)+"  "+periodo)
                    plt.xticks(rotation='vertical')
                    plt.gcf().subplots_adjust(bottom=0.50)
                    fig.savefig("../plots/"+folder+"/"+dividendo+"/"+periodo+"/"+target+" "+str(anno)+" "+periodo+".png")
                    plt.close()


"""
os.mkdir("../plots")
migliori(df_piccoli,"piccoli")
migliori(df_medi,"medi")
migliori(df_grandi,"grandi")
migliori(df_enormi,"enormi")
migliori(df_megalopoli,"megalopoli")
"""


FF=df_piccoli[df_piccoli["anno"]==2016]
df_piccoli[df_piccoli["anno"]==2017]["totale_n+r"]
piccoli=df_piccoli["delegazione"].to_numpy()
piccoli=np.unique(piccoli)
piccoli.shape
df_piccoli
FF
df.columns

lista_df=[df_piccoli,df_medi, df_grandi,df_enormi,df_megalopoli]

def assoluti(item,denominatore,lista_df,df):
    try:
        os.mkdir("../plots/torte valori assoluti")
    except OSError:
        pass
    periodi=["GFP","GFA"]
    anni=[2016,2017,2018,2019]
    perc=[]
    labels=["piccoli","medi","grandi", "enormi", "magalopoli"]
    for anno in anni:
        for periodo in periodi:
            for d in lista_df:
                d_tot=df.copy(deep=True)
                d_tot=d_tot[d_tot["anno"]==anno]
                d_tot=d_tot[d_tot["tipo"]==periodo]
                dd=d.copy(deep=True)
                dd=dd[dd["anno"]==anno]
                dd=dd[dd["tipo"]==periodo]
                perc.append(sum(dd[item]))
            fig1, ax1 = plt.subplots()
            ax1.pie(perc, labels=labels, autopct='%1.1f%%', startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            perc=[]
            plt.title(item+" "+str(anno)+" "+periodo)
            plt.savefig("../plots/torte valori assoluti/"+item+" "+str(anno)+" "+periodo)
            plt.show()


assoluti("totale_n+r",lista_df,df)
assoluti("tot_entrate",lista_df,df)


def relativi(item,denominatore,lista_df,df,save=False):
    if save==True:
        try:
            os.mkdir("../plots/torte valori relativi")
        except OSError:
            print("non ho combinato")
            pass
        try:
            os.mkdir("../plots/torte valori relativi/"+item+" su "+denominatore)
        except OSError:
            pass
    periodi=["GFP","GFA"]
    anni=[2016,2017,2018,2019]
    bar=[]
    labels=["piccoli","medi","grandi", "enormi", "magalopoli"]
    for anno in anni:
        for periodo in periodi:
            for d in lista_df:
                d_tot=df.copy(deep=True)
                d_tot=d_tot[d_tot["anno"]==anno]
                d_tot=d_tot[d_tot["tipo"]==periodo]
                dd=d.copy(deep=True)
                dd=dd[dd["anno"]==anno]
                dd=dd[dd["tipo"]==periodo]
                bar.append(sum(dd[item])/sum(dd[denominatore]))
            plt.bar(labels,bar)
            bar=[]
            plt.title(item+" "+str(anno)+" "+periodo)
            if save==True:
                plt.savefig("../plots/torte valori relativi/"+item+" su "+denominatore+"/"+item+"-"+denominatore+" "+str(anno)+" "+periodo)
            plt.show()
relativi("tot_entrate","densità",lista_df,df,save=True)
relativi("totale_n+r","densità",lista_df,df,save=True)




def scatter_plot(item_1,item_2,lista_df,save=False):
    if save==True:
        try:
            os.mkdir("../plots/scatter")
        except OSError:
            print("non ho combinato")
            pass

    periodi=["GFP","GFA"]
    anni=[2016,2017,2018,2019]

    labels=["piccoli","medi","grandi", "enormi", "magalopoli"]
    i=0
    for anno in anni:
        for periodo in periodi:
            for dd in lista_df:
                d=dd.copy(deep=True)
                #d=d[d["tot_entrate"]>10000]
                try:
                    x=np.mean(d[item_1]/d["abitanti"])
                    plt.plot([x,x],[0,max(d[item_2]/d["abitanti"])],color="red",linewidth=2)
                    y=np.mean(d[item_2]/d["abitanti"])
                    plt.plot([0,max(d[item_1]/d["abitanti"])],[y,y],color="green",linewidth=2)
                    plt.scatter(d[item_1]/d["abitanti"],d[item_2]/d["abitanti"])
                    plt.title(item_2+" su "+item_1+str(anno)+" "+periodo+" "+labels[i])
                    if save==True:
                        plt.savefig("../plots/scatter/"+item_1+" su "+item_2+" "+str(anno)+" "+periodo+ " "+labels[i])
                    plt.show()
                except:
                    pass
                i+=1
            i=0


scatter_plot("volontari","tot_entrate",lista_df,save=True)


d=df.copy(deep=True)


x=np.mean(d["luoghi_aperti"]/d["abitanti"])
plt.plot([x,x],[0,max(d["tot_entrate"]/d["abitanti"])],color="red",linewidth=2)
y=np.mean(d["tot_entrate"]/d["abitanti"])
plt.plot([0,max(d["luoghi_aperti"]/d["abitanti"])],[y,y],color="green",linewidth=2)
plt.scatter(d["luoghi_aperti"]/d["abitanti"],d["tot_entrate"]/d["abitanti"])
plt.title("globale diviso num abitanti")
plt.savefig("../plots/scatter/globale.png")







def migliori_2(df_local_in,df_title,best,threshold=0,save=False):
    if save==True:
        try:
            os.mkdir("../plots/best")
        except OSError:
            pass

    dividendi=["tot_entrate","totale_n+r"]
    targets=["abitanti"]
    periodi=["GFA"]
    df_local=df_local_in.copy(deep=True)
    df_local=df_local[df_local["tot_entrate"]>threshold]
    for dividendo in dividendi:
        if save==True:
            try:
                os.mkdir("../plots/best/"+dividendo)
            except OSError:
                pass
        for periodo in periodi:
            if save==True:
                try:
                    os.mkdir("../plots/best/"+dividendo+"/"+periodo)
                except OSError:
                    pass
            for target in targets:
                for anno in np.unique(df_local["anno"].to_numpy()):
                    if anno!=2016:
                        fig=plt.figure()
                        df_to_plot=df_local[df_local["tipo"]==periodo]
                        df_to_plot=df_to_plot[df_to_plot["anno"]==anno]
                        df_to_plot["target"]=df_to_plot[dividendo]/df_to_plot[target]
                        df_to_plot.sort_values(by="target",ascending=False,inplace=True)
                        df_to_plot=df_to_plot.iloc[:best]
                        plt.bar((df_to_plot['delegazione'].values).astype(str),df_to_plot["target"])
                        plt.title(dividendo+" su "+target+"  "+str(anno)+"  "+periodo+" "+df_title)
                        plt.xticks(rotation='vertical')
                        plt.gcf().subplots_adjust(bottom=0.50)
                        if save==True:
                            fig.savefig("../plots/best/"+dividendo+"/"+periodo+"/"+target+" "+str(anno)+" "+periodo+".png")
                            plt.close()
                        else:
                            plt.show()

labels=["piccoli","medi","grandi", "enormi", "magalopoli"]
for i in range(len(lista_df)):
    migliori_2(lista_df[i],labels[i],20)
    
