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
