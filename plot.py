import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
import data as dt


df=pd.read_csv("dati/df_fai.csv", sep=",")
df.columns=[i.lower() for i in df.columns]
df.columns=[i if "/" not in i else i.replace("/","-") for i in df.columns]
df.columns=[i if "€" not in i else i.replace("€","eur") for i in df.columns]
df.columns=[i if "%" not in i else i.replace("%","perc") for i in df.columns]

df.columns

df.sort_values(by="abitanti",ascending=False)

df_abitanti=df.copy(deep=True)



df_abitanti=df_abitanti[df_abitanti["abitanti"]<150000]
df_abitanti.drop_duplicates("delegazione",inplace=True)
df_abitanti.shape
df_abitanti.sort_values(by="abitanti",ascending=False,inplace=True)
mlt.rcParams["figure.figsize"]=(20,10)
mlt.rcParams["font.size"]=20
plt.plot(np.arange(df_abitanti.shape[0]),df_abitanti["abitanti"])
plt.hist(df_abitanti["abitanti"],bins=20)
plt.hist(df_abitanti["abitanti"],bins=30)


df_piccoli=df[df["abitanti"]<20000]

df_medi=df[df["abitanti"]<100000]
df_medi=df_medi[df_medi["abitanti"]>=20000]

df_grandi=df[df["abitanti"]<400000]
df_grandi=df_grandi[df_grandi["abitanti"]>=100000]

df_enormi=df[df["abitanti"]>=400000]
df_enormi=df_enormi[df_enormi["abitanti"]<1000000]

df_megalopoli=df[df["abitanti"]>=1000000]
df_megalopoli.iloc[:20]

np.unique(df["anno"].to_numpy())


def migliori(df_local,folder):
    %matplotlib agg
    plt.ioff()
    dividendi=["tot_entrate","totale_n+r","ctb_visitatori"]
    targets=["luoghi_aperti","visitatori","abitanti","densità","reddito medio"]
    periodi=["GFP","GFA"]
    for dividendo in dividendi:
        for periodo in periodi:
            for target in targets:
                for anno in np.unique(df_local["anno"].to_numpy()):
                    df_primavera=df_local[df_local["tipo"]==periodo]
                    df_primavera=df_primavera[df_primavera["anno"]==anno]
                    df_primavera["target"]=df_primavera[dividendo].astype(float)/df_primavera[target]
                    df_primavera.sort_values(by="target",ascending=False,inplace=True)
                    df_primavera=df_primavera.iloc[:20]
                    plt.bar((df_primavera['delegazione'].values).astype(str),df_primavera["target"])
                    plt.title(target+"  "+str(anno)+"  "+periodo)
                    plt.xticks(rotation='vertical')
                    plt.gcf().subplots_adjust(bottom=0.50)
                    plt.savefig("plots/"+folder+"/"+dividendo+"/"+dividendo+"-"+target+" "+str(anno)+" "+periodo+".png")
                    plt.show()


migliori(df_piccoli,"piccoli")
migliori(df_medi,"medi")
migliori(df_grandi,"grandi")
migliori(df_enormi,"enormi")
migliori(df_megalopoli,"megalopoli")


for i in df_piccoli["ctb_visitatori"]:
    print(i)

df_piccoli["ctb_visitatori"]/df_piccoli["luoghi_aperti"]
df_piccoli["ctb_visitatori"].astype(float)
