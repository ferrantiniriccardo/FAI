import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
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

    cols=["black","green","yellow","red","blue","gray"]
    colors=[]
    for i in range(df_local.shape[0]):
        j=0
        while j<len(th) and df_local.iloc[i]["abitanti"]>th[j]:
            j+=1
        colors.append(cols[j-1])
    return colors
