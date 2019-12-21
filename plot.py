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

os.mkdir("../plots")
migliori(df_piccoli,"piccoli")
migliori(df_medi,"medi")
migliori(df_grandi,"grandi")
migliori(df_enormi,"enormi")
migliori(df_megalopoli,"megalopoli")
