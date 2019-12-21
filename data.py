import pandas as pd
import numpy as np


df=pd.read_csv("dati/dati_row.csv",sep=";")

df.columns=[i.lower() for i in df.columns]
df.columns=[i if "/" not in i else i.replace("/","-") for i in df.columns]
df.columns=[i if "€" not in i else i.replace("€","eur") for i in df.columns]
df.columns=[i if "%" not in i else i.replace("%","perc") for i in df.columns]

df_comuni=pd.read_csv("dati/dati_comuni.csv",sep=";")
df_comuni.columns=[i.lower() for i in df_comuni.columns]
df["delegazione"]=[i.replace("_"," " ) for i in df["delegazione"].values]
df


def cd(luogo,dict):
    trovate=[]
    luogo=luogo.lower()
    for key in dict:
        if luogo in key.lower():
            trovate.append(key)
    return trovate


def make_dict_delegazioni():
    dict_delegazioni={}
    for i in range(df_comuni.shape[0]):
        if df_comuni.iloc[i]["delegazione"] not in dict_delegazioni:
            dict_delegazioni[df_comuni.iloc[i]["delegazione"]]=0
    return dict_delegazioni

def fill_dict_delegazioni(dict_delegazioni):
    for key in dict_delegazioni:
        dict_delegazioni[key]=sum(df_comuni[df_comuni["delegazione"]==key]["pop istat"].values.astype(int))
    return dict_delegazioni



dict_delegazioni=make_dict_delegazioni()
dict_delegazioni=fill_dict_delegazioni(dict_delegazioni)
dict_delegazioni
dict_del_per_df=dict(zip(df["delegazione"].values,np.zeros(df.shape[0])))

len(dict_del_per_df)
len(dict_delegazioni)

def fill_dict_del(dict_del_per_df,dict_delegazioni):
    mancanti=[]
    for delegazione in dict_del_per_df:
        deleg=cd(delegazione,dict_delegazioni)
        if len(deleg)==1:
            dict_del_per_df[delegazione]=dict_delegazioni[deleg[0]]
        else:
            mancanti.append((delegazione,deleg))
    return dict_del_per_df,mancanti

dict_del_per_df,mancanti=fill_dict_del(dict_del_per_df,dict_delegazioni)
len(dict_delegazioni)
len(mancanti)
mancanti
d=list(dict_del_per_df.keys())
d.sort()
cd("crotone",dict_delegazioni)
len(d)
d=[i.replace("Delegazione ","") for i in d]
d=[i.replace("di ","") for i in d]
d=[i.replace("de ","") for i in d]
d=[i.replace("del ","") for i in d]
d=[i.replace("della ","") for i in d]
d=[i.replace("FAI ","") for i in d]
d.sort()
d=list(dict.fromkeys(d))
d
df[df["regione"]=="Calabria"]
