import funzioni as fun
import coorti as coo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlt
import os

df,little,middle_1,middle_2,middle_3,middle,big,huge,all_no_little,thresholds,thresholds_short=coo.make_all_df()




def assoluti_medie(item,lista_df,labels,df,save=False):
    if save==True:
        try:
            os.mkdir("../plots/torte valori assoluti medie")
        except OSError:
            pass

    perc=[]

    for d in lista_df:
        perc.append(sum(d[item]))
    fig1, ax1 = plt.subplots()
    ax1.pie(perc, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(item+" media")
    if save==True:
        plt.savefig("../plots/torte valori assoluti medie/"+item)
    plt.show()


lista_df=[little,middle_1,middle_2,middle_3,big,huge]
labels=["piccoli","medi 1","medi 2","medi 3","grandi", "metropoli"]
assoluti_medie("tot_entrate",lista_df,labels,df,save=True)
assoluti_medie("totale_n+r",lista_df,labels,df,save=True)

lista_df=[little,middle,big,huge]
labels=["piccoli","medi","grandi", "metropoli"]
assoluti_medie("tot_entrate",lista_df,labels,df)
assoluti_medie("totale_n+r",lista_df,labels,df)




def tot_pop_medie(item,lista_df,labels,df,save=False):
    if save==True:
        try:
            os.mkdir("../plots/"+str(item)+" popolazione medie")
        except OSError:
            pass
    perc=np.array([])
    pop_perc=np.array([])
    colors=["black","red","blue","yellow"]

    for d in lista_df:
        perc=np.append(perc,sum(d[item])/sum(df[item]))
        pop_perc=np.append(pop_perc,sum(d["abitanti"])/sum(df["abitanti"]))

    x=np.array([0])
    x=np.append(x,np.cumsum(pop_perc[:-1]))
    plt.bar(x,perc,width=pop_perc,align='edge',color=colors)
    x=[(x[i]+ x[i+1])/2 for i in range(len(x)-1)]
    x=np.append(x,(np.cumsum(pop_perc)[-2]+np.cumsum(pop_perc)[-1])/2)
    plt.xticks(x,labels)
    plt.title(item+" media")
    if save==True:
        plt.savefig("../plots/"+str(item)+" popolazione medie/"+item+" confrontato con popolazione  ")
    plt.show()



lista_df=[little,middle_1,middle_2,middle_3,big,huge]
labels=["piccoli","medi 1","medi 2","medi 3","grandi", "metropoli"]
tot_pop_medie("tot_entrate",lista_df,labels,df,save=True)
tot_pop_medie("totale_n+r",lista_df,labels,df)

lista_df=[little,middle,big,huge]
labels=["piccoli","medi","grandi", "metropoli"]
tot_pop_medie("tot_entrate",lista_df,labels,df,save=True)
tot_pop_medie("totale_n+r",lista_df,labels,df)







def tot_delegazioni_medie(item,lista_df,labels,df,primavera_autunno=True,save=False):
    if save==True:
        try:
            os.mkdir("../plots/"+str(item)+" delegazoni medie")
        except OSError:
            pass
    perc=np.array([])
    del_perc=np.array([])
    colors=["black","red","blue","yellow"]


    for d in lista_df:

        perc=np.append(perc,sum(d[item])/sum(df[item]))
        del_perc=np.append(del_perc,d.shape[0]/df.shape[0])

    x=np.array([0])
    x=np.append(x,np.cumsum(del_perc[:-1]))
    plt.bar(x,perc,width=del_perc,align='edge',color=colors)
    x=[(x[i]+ x[i+1])/2 for i in range(len(x)-1)]
    x=np.append(x,(np.cumsum(del_perc)[-2]+np.cumsum(del_perc)[-1])/2)
    plt.xticks(x,labels)
    perc=[]
    del_perc=[]
    plt.title(item+" delegazioni ")
    if save==True:
        plt.savefig("../plots/"+str(item)+" delegazoni medie/"+item+" confrontato con num delegazioni.png")
    plt.show()


lista_df=[little,middle_1,middle_2,middle_3,big,huge]
labels=["piccoli","medi 1","medi 2","medi 3","grandi", "metropoli"]
tot_delegazioni_medie("tot_entrate",lista_df,labels,df)
tot_delegazioni_medie("totale_n+r",lista_df,labels,df)

lista_df=[little,middle,big,huge]
labels=["piccoli","medi","grandi", "metropoli"]
tot_delegazioni_medie("tot_entrate",lista_df,labels,df,save=True)
tot_delegazioni_medie("totale_n+r",lista_df,labels,df)
