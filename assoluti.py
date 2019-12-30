import funzioni as fun
import coorti as coo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlt
import os

df,little,middle_1,middle_2,middle_3,middle,big,huge,all_no_little,thresholds,thresholds_short=coo.make_all_df()




def assoluti(item,lista_df,labels,df,save=False):
    """
        Pie chart dell'apporto in termini assoluti delle varie coorti all'item in esame
    """
    if save==True:
        try:
            os.mkdir("../plots/torte valori assoluti")
        except OSError:
            pass
        try:
            os.mkdir("../plots/torte valori assoluti/nuovi")
        except OSError:
            pass
    periodi=["GFP","GFA"]
    anni=[2016,2017,2018,2019]
    perc=[]

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
            if save==True:
                plt.savefig("../plots/torte valori assoluti/nuovi/"+item+" "+str(anno)+" "+periodo)
            plt.show()


lista_df=[little,middle_1,middle_2,middle_3,big,huge]
labels=["piccoli","medi 1","medi 2","medi 3","grandi", "metropoli"]
assoluti("tot_entrate",lista_df,labels,df,save=True)
assoluti("totale_n+r",lista_df,labels,df)

lista_df=[little,middle,big,huge]
labels=["piccoli","medi","grandi", "metropoli"]
assoluti("tot_entrate",lista_df,labels,df)
assoluti("totale_n+r",lista_df,labels,df)




def tot_pop(item,lista_df,labels,df,save=False):
    """
        Bar plot. Altezza: indicatore percentuale item per coorte.
                  Larghezza: percentuale popolazione di riferimento
    """
    if save==True:
        try:
            os.mkdir("../plots/"+str(item)+" popolazione ")
        except OSError:
            pass
    periodi=["GFP","GFA"]
    anni=[2016,2017,2018,2019]
    perc=np.array([])
    pop_perc=np.array([])
    colors=["black","red","blue","yellow"]

    for anno in anni:
        for periodo in periodi:
            for d in lista_df:
                d_tot=df.copy(deep=True)
                d_tot=d_tot[d_tot["anno"]==anno]
                d_tot=d_tot[d_tot["tipo"]==periodo]
                dd=d.copy(deep=True)
                dd=dd[dd["anno"]==anno]
                dd=dd[dd["tipo"]==periodo]
                perc=np.append(perc,sum(dd[item])/sum(d_tot[item]))
                pop_perc=np.append(pop_perc,sum(dd["abitanti"])/sum(df[df["anno"]==anno]["abitanti"]))

            x=np.array([0])
            x=np.append(x,np.cumsum(pop_perc[:-1]))
            plt.bar(x,perc,width=pop_perc,align='edge',color=colors)
            x=[(x[i]+ x[i+1])/2 for i in range(len(x)-1)]
            x=np.append(x,(np.cumsum(pop_perc)[-2]+np.cumsum(pop_perc)[-1])/2)
            plt.xticks(x,labels)
            perc=[]
            pop_perc=[]
            plt.title(item+" "+str(anno)+" "+periodo)
            if save==True:
                plt.savefig("../plots/"+str(item)+" popolazione /"+item+" confrontato con popolazione  "+str(anno)+" "+periodo)
            plt.show()



lista_df=[little,middle_1,middle_2,middle_3,big,huge]
labels=["piccoli","medi 1","medi 2","medi 3","grandi", "metropoli"]
tot_pop("tot_entrate",lista_df,labels,df,save=True)
tot_pop("totale_n+r",lista_df,labels,df)

lista_df=[little,middle,big,huge]
labels=["piccoli","medi","grandi", "metropoli"]
tot_pop("tot_entrate",lista_df,labels,df)
tot_pop("totale_n+r",lista_df,labels,df)







def tot_delegazioni(item,lista_df,labels,df,save=False):
    """
        Bar plot. Altezza: indicatore percentuale item per coorte.
                  Larghezza: percentuale delegazioni di riferimento
    """
    if save==True:
        try:
            os.mkdir("../plots/"+str(item)+" delegazoni ")
        except OSError:
            pass
    periodi=["GFP","GFA"]
    anni=[2016,2017,2018,2019]
    perc=np.array([])
    del_perc=np.array([])
    colors=["black","red","blue","yellow"]

    for anno in anni:
        for periodo in periodi:
            for d in lista_df:
                d_tot=df.copy(deep=True)
                d_tot=d_tot[d_tot["anno"]==anno]
                d_tot=d_tot[d_tot["tipo"]==periodo]
                dd=d.copy(deep=True)
                dd=dd[dd["anno"]==anno]
                dd=dd[dd["tipo"]==periodo]
                perc=np.append(perc,sum(dd[item])/sum(d_tot[item]))
                del_perc=np.append(del_perc,dd.shape[0]/d_tot.shape[0])

            x=np.array([0])
            x=np.append(x,np.cumsum(del_perc[:-1]))
            plt.bar(x,perc,width=del_perc,align='edge',color=colors)
            x=[(x[i]+ x[i+1])/2 for i in range(len(x)-1)]
            x=np.append(x,(np.cumsum(del_perc)[-2]+np.cumsum(del_perc)[-1])/2)
            plt.xticks(x,labels)
            perc=[]
            del_perc=[]
            plt.title(item+" "+str(anno)+" "+periodo)
            if save==True:
                plt.savefig("../plots/"+str(item)+" delegazioni /"+item+" confrontato con num delegazioni  "+str(anno)+" "+periodo)
            plt.show()


lista_df=[little,middle_1,middle_2,middle_3,big,huge]
labels=["piccoli","medi 1","medi 2","medi 3","grandi", "metropoli"]
tot_delegazioni("tot_entrate",lista_df,labels,df)
tot_delegazioni("totale_n+r",lista_df,labels,df)

lista_df=[little,middle,big,huge]
labels=["piccoli","medi","grandi", "metropoli"]
tot_delegazioni("tot_entrate",lista_df,labels,df)
tot_delegazioni("totale_n+r",lista_df,labels,df)
