import funzioni as fun
import coorti as coo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mlt
import os




df,little,middle_1,middle_2,middle_3,middle,big,huge,all_no_little,thresholds,thresholds_short=coo.make_all_df()

def ranking_gruppi_media(item,lista_df,labels,df,save=False):
    if save==True:
        try:
            os.mkdir("../plots/"+str(item)+" ranking gruppi medie")
        except OSError:
            pass
    efficienza=np.array([])
    colors=["black","red","blue","yellow","green"]

    for d in lista_df:
        efficienza=np.append(efficienza,sum(d[item])/sum(d["abitanti"]))

    sort_index=np.argsort(efficienza)
    efficienza=np.sort(efficienza)
    labels_sorted=[labels[sort_index[i]] for i in range(len(labels))]
    plt.bar(labels_sorted,efficienza,color=colors)

    plt.title(item+" ranking gruppi media")
    if save==True:
        plt.savefig("../plots/"+str(item)+" ranking gruppi medie/"+item+" confrontato con popolazione  ")
    plt.show()



lista_df=[middle_1,middle_2,middle_3,big,huge]
labels=["medi 1","medi 2","medi 3","grandi", "metropoli"]
ranking_gruppi_media("tot_entrate",lista_df,labels,df)
ranking_gruppi_media("totale_n+r",lista_df,labels,df)



lista_df=[middle,big,huge]
labels=["medi","grandi", "metropoli"]
ranking_gruppi_media("tot_entrate",lista_df,labels,df)
ranking_gruppi_media("totale_n+r",lista_df,labels,df)



fun.cerca_delegazione("ancona",df)
ancona=df[df["delegazione"]=="Delegazione Ancona"]
ancona=ancona.append(df[df["delegazione"]=="Delegazione FAI Ancona"])
ancona

vimerc=fun.cerca_delegazione("mercatese",df)

vi=df[df["delegazione"]==vimerc[0]]
for v in vimerc[1:]:
    vi=vi.append(df[df["delegazione"]==v])
vi
