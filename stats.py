import numpy as np
import matplotlib.pyplot as plt
import to_df as data
import copy


df=data.make_df("Consuntivo_GFP_2019.csv")
df=df[df["DELEGAZIONE-GRUPPO"]!="Delegazione FAI di Parma"]






def print_voci():
    items=df.columns
    for i in range(len(items)):
        print(i,items[i])

def cerca_delegazione(luogo):
    trovate=[]
    luogo=luogo.lower()
    delegazioni=list(df["DELEGAZIONE-GRUPPO"].values)
    delegazioni=[string.lower() for string in delegazioni]
    for i in range(len(delegazioni)):
        for j in range(len(luogo),int(len(luogo)*2/3),-1):
            if luogo[:j] in delegazioni[i]:
                if df["DELEGAZIONE-GRUPPO"].values[i] not in trovate:
                    trovate.append(df["DELEGAZIONE-GRUPPO"].values[i])
    return trovate

def hist_rapporto_popolazione(item,migliori_N,save=False):
    N=migliori_N

    df_provvisorio=copy.deepcopy(df)
    df_provvisorio['new_col']=(df[item].values).astype(float)/df['POPOLAZIONE'].values
    df_provvisorio.sort_values('new_col',inplace=True,ascending=False)
    df_provvisorio.reset_index(inplace = True,drop=True)
    df_provvisorio=df_provvisorio.head(N)
    plt.figure(figsize=(16,16))
    plt.rc('font',size=25)
    plt.bar((df_provvisorio['DELEGAZIONE-GRUPPO'].values).astype(str),df_provvisorio['new_col'])
    plt.title("Rapporto "+item+"/Popolazione (Migliori "+str(N)+")")
    plt.xticks(rotation='vertical')
    plt.gcf().subplots_adjust(bottom=0.50)
    if save==True:
        plt.savefig(item+"-pop.png")
    else:
        plt.show()



def ranking_FAI_popolazione(delegazione):
    item=df.columns
    rank={}
    for i in [1,2,4,8,20]:
        df_provvisorio=copy.deepcopy(df)
        df_provvisorio['new_col']=(df[item[i]].values).astype(float)/df['POPOLAZIONE'].values
        df_provvisorio.sort_values('new_col',inplace=True,ascending=False)
        df_provvisorio.reset_index(inplace = True,drop=True)
        row=df_provvisorio.loc[df_provvisorio['DELEGAZIONE-GRUPPO'] ==delegazione]
        rank[item[i]]=(str(row.index.values.astype(int)[0]+1)+"°",row[item[i]].values[0])
    print("\n\n"+delegazione+": ranking relativo\n")
    for key in rank:
        print('{:>40}'.format(key),"   posizione: ",'{:>4}'.format(rank[key][0]),"     valore: ",rank[key][1])
    return rank



def hist_rapporto(item,item_relativo,migliori_N,save=False):
    N=migliori_N

    df_provvisorio=copy.deepcopy(df)
    df_provvisorio['new_col']=(df[item].values).astype(float)/df[item_relativo].values.astype(float)
    df_provvisorio.sort_values('new_col',inplace=True,ascending=False)
    df_provvisorio.reset_index(inplace = True,drop=True)
    df_provvisorio=df_provvisorio.head(N)
    plt.figure(figsize=(16,16))
    plt.rc('font',size=25)
    plt.bar((df_provvisorio['DELEGAZIONE-GRUPPO'].values).astype(str),df_provvisorio['new_col'])
    plt.title("Rapporto "+item+"/"+item_relativo+" (Migliori "+str(N)+")")
    plt.xticks(rotation='vertical')
    plt.gcf().subplots_adjust(bottom=0.50)
    if save==True:
        plt.savefig(item+"-"+item_relativo +".png")
    else:
        plt.show()

def ranking_FAI(delegazione):
    item=df.columns
    rank={}
    for i in [1,2,4,8,20]:
        df_provvisorio=copy.deepcopy(df)
        df_provvisorio['new_col']=(df[item[i]].values).astype(float)
        df_provvisorio.sort_values('new_col',inplace=True,ascending=False)
        df_provvisorio.reset_index(inplace = True,drop=True)
        row=df_provvisorio.loc[df_provvisorio['DELEGAZIONE-GRUPPO'] ==delegazione]
        rank[item[i]]=(str(row.index.values.astype(int)[0]+1)+"°",row[item[i]].values[0])
    print("\n\n\n"+delegazione+": ranking assoluto\n")
    for key in rank:
        print('{:>40}'.format(key),"   posizione: ",'{:>4}'.format(rank[key][0]),"     valore: ",rank[key][1])
    return rank



cerca_delegazione("castello")

items=df.columns
print_voci()
hist_rapporto_popolazione(items[22],15)
PN_rel=ranking_FAI_popolazione("Delegazione FAI di Pordenone")
PN=ranking_FAI("Delegazione FAI di Pordenone")

k=ranking_FAI(cerca_delegazione("onferrato")[1])
k=ranking_FAI(cerca_delegazione("nicosia")[0])
k=ranking_FAI(cerca_delegazione("Pordenone")[0])
cerca_delegazione("roma")


hist_rapporto(items[8],items[31],20)

df[df["DELEGAZIONE-GRUPPO"]==cerca_delegazione("castello")[1]]["POPOLAZIONE"].values[0]

df[df["DELEGAZIONE-GRUPPO"]==cerca_delegazione("pordenone")[0]]
cerca_delegazione("porde")[0]
df.sort_values(items[22],ascending=True).head(50)

170/312000

170/13000
