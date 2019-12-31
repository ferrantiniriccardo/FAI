import funzioni as fun
import coorti as coo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mlt
import os

df,little,middle_1,middle_2,middle_3,middle,big,huge,all_no_little,thresholds,thresholds_short=coo.make_all_df()


def andamento(item,df_lista,labels):

    curva=np.array([])

    anni=[2016,2017,2018,2019]
    periodi=["GFP","GFA"]
    i=0
    for d in df_lista:
        for anno in anni:
            for periodo in periodi:
                dd=d.copy(deep=True)
                dd=dd[dd["anno"]==anno]
                dd=dd[dd["tipo"]==periodo]
                curva=np.append(curva,sum(dd[item]))
        plt.plot(curva,label=labels[i])
        i+=1
        curva=np.array([])
    plt.legend()
    plt.show()


lista_df=[middle_1,middle_2,middle_3,big,huge]
labels=["medi 1","medi 2","medi 3","grandi", "metropoli"]
andamento("tot_entrate",lista_df,labels)
andamento("totale_n+r",lista_df,labels)


lista_df=[little,middle,big,huge]
labels=["piccoli","medi","grandi", "metropoli"]
andamento("tot_entrate",lista_df,labels)
andamento("totale_n+r",lista_df,labels)




# genearle entrate
to_plot=np.array([])
for anno in [2016,2017,2018,2019]:
    to_plot=np.append(to_plot,sum(df[df["anno"]==anno]["tot_entrate"]))
plt.title("Andamento generale entrate")
plt.xticks([2016,2017,2018,2019])
plt.plot([2016,2017,2018,2019],to_plot, color="red")
plt.savefig("../plots/andamenti/generale entrate.png")


#generale tessere
to_plot=np.array([])
for anno in [2016,2017,2018,2019]:
    to_plot=np.append(to_plot,sum(df[df["anno"]==anno]["totale_n+r"]))
plt.title("Andamento generale entrate")
plt.xticks([2016,2017,2018,2019])
plt.plot([2016,2017,2018,2019],to_plot, color="red")
plt.savefig("../plots/andamenti/generale tessere.png")




# genearle entrate
to_plot=np.array([])
for anno in [2016,2017,2018,2019]:
    d=df[df["anno"]==anno]
    for periodo in ["GFP","GFA"]:
        to_plot=np.append(to_plot,sum(d[d["tipo"]==periodo]["tot_entrate"]))
plt.title("Andamento generale gfp/gfa")
plt.xticks(range(8),labels=["2016 gfp","2016 gfa","2017 gfp","2017 gfa","2018 gfp","2018 gfa","2019 gfp", "2019 gfa"])
plt.plot(to_plot, color="red")
plt.savefig("../plots/andamenti/generale entrate gfp vs gfa.png")


#generale tessere
to_plot=np.array([])

for anno in [2016,2017,2018,2019]:
    d=df[df["anno"]==anno]
    for periodo in ["GFP","GFA"]:
        to_plot=np.append(to_plot,sum(d[d["tipo"]==periodo]["tot_entrate"]))
plt.title("Andamento generale gfp/gfa")
plt.xticks(range(8),["2016 gfp","2016 gfa","2017 gfp","2017 gfa","2018 gfp","2018 gfa","2019 gfp", "2019 gfa"])
plt.plot(to_plot, color="red")
plt.savefig("../plots/andamenti/generale tessere gfp vs gfa.png")
