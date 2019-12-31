import funzioni as fun
import coorti as coo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mlt
import modello as md
import os




df,little,middle_1,middle_2,middle_3,middle,big,huge,all_no_little,thresholds,thresholds_short=coo.make_all_df()

def ranking_gruppi_media(item,k,n,lista_df,labels,df,save=False):
    if save==True:
        try:
            os.mkdir("../plots/"+str(item)+" ranking gruppi medie")
        except OSError:
            pass
    efficienza=np.array([])
    if len(labels)==4:
        colors=np.array(["deepskyblue","orange","g","fuchsia"])
    else:
        colors=np.array(["deepskyblue","#f5b303","orange","darkorange","g","fuchsia"])

    for d in lista_df:
        efficienza=np.append(efficienza,sum(d[item]/(k*d["abitanti"])**n))

    sort_index=np.argsort(efficienza)
    efficienza=np.sort(efficienza)
    labels_sorted=[labels[sort_index[i]] for i in range(len(labels))]
    plt.bar(labels_sorted,efficienza,color=colors)

    plt.title(item+" ranking gruppi media")
    if save==True:
        plt.savefig("../plots/"+str(item)+" ranking gruppi medie/"+item+" confrontato con popolazione  ")
    plt.show()



k,n=md.fit_model()


lista_df=[little,middle_1,middle_2,middle_3,big,huge]
labels=["piccoli","medi 1","medi 2","medi 3","grandi", "metropoli"]
ranking_gruppi_media("tot_entrate",k,n,lista_df,labels,df)
ranking_gruppi_media("totale_n+r",k,n,lista_df,labels,df)



lista_df=[little,middle,big,huge]
labels=["piccoli","medi","grandi", "metropoli"]
ranking_gruppi_media("tot_entrate",k,n,lista_df,labels,df)
ranking_gruppi_media("totale_n+r",lista_df,labels,df)
