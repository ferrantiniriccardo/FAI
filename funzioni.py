import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
from scipy import stats
import os


def cerca_delegazione(luogo,df):
    trovate=[]
    luogo=luogo.lower()
    delegazioni=list(df["delegazione"].values)
    delegazioni=[string.lower() for string in delegazioni]
    for i in range(len(delegazioni)):
        for j in range(len(luogo),int(len(luogo)*2/3),-1):
            if luogo[:j] in delegazioni[i]:
                if df["delegazione"].values[i] not in trovate:
                    trovate.append(df["delegazione"].values[i])
    return trovate



def set_colors(df_local, th):
    th=np.array(th)
    th=np.insert(th,0,0)

    colors=np.array([])

    if len(th)==6:
        color_list=np.array(["deepskyblue","#f5b303","orange","darkorange","g","fuchsia"])
        labels=["piccoli","medi 1","medi 2","medi 3", "grandi", "metropoli"]
        for i in range(df_local.shape[0]):
            j=0
            while j<len(th) and df_local.iloc[i]["abitanti"]>th[j]:
                j+=1
            colors=np.append(colors,color_list[j-1])
    else:
        color_list=np.array(["deepskyblue","orange","g","fuchsia"])
        labels=["piccoli","medi", "grandi", "metropoli"]
        for i in range(df_local.shape[0]):
            j=0
            while j<len(th) and df_local.iloc[i]["abitanti"]>th[j]:
                j+=1
            colors=np.append(colors,color_list[j-1])
    return colors,color_list,labels


def make_df_training():
    df=pd.read_csv("dati/df_fai.csv", sep=",")
    df.columns=[i.lower() for i in df.columns]
    df.columns=[i if "/" not in i else i.replace("/","-") for i in df.columns]
    df.columns=[i if "€" not in i else i.replace("€","eur") for i in df.columns]
    df.columns=[i if "%" not in i else i.replace("%","perc") for i in df.columns]


    delegazioni=np.unique(df["delegazione"])
    delegazioni=delegazioni[delegazioni!="Delegazione Roma"]

    df_test=df[df["delegazione"]=="Delegazione Roma"]


    for deleg in delegazioni:
        df_aux=df[df["delegazione"]==deleg]
        value,cardinality=stats.mode(df_aux["abitanti"])
        if cardinality[0]>2:
            df_test=df_test.append(df_aux[df_aux["abitanti"]==value[0]])


            #df_test=df_test[df_test["abitanti"]<1250000]

    return df_test
