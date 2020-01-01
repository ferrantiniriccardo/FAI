import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
import os
import funzioni as fun


mlt.rcParams["figure.figsize"]=(40,20)
mlt.rcParams["font.size"]=40


def bins_labels(bins, **kwargs):
    bin_w = (max(bins) - min(bins)) / (len(bins) - 1)
    plt.xticks(np.arange(min(bins)+bin_w/2, max(bins), bin_w), bins, **kwargs)
    plt.xlim(bins[0], bins[-1])




def make_all_df(save=False):

    df=pd.read_csv("dati/df_fai.csv", sep=",")
    df.columns=[i.lower() for i in df.columns]
    df.columns=[i if "/" not in i else i.replace("/","-") for i in df.columns]
    df.columns=[i if "€" not in i else i.replace("€","eur") for i in df.columns]
    df.columns=[i if "%" not in i else i.replace("%","perc") for i in df.columns]

    if save==True:
        try:
            os.mkdir("../plots/divisione coorti")
        except OSError:
            pass



    df_abitanti=df.copy(deep=True)

    df_abitanti=df_abitanti.sort_values(by="abitanti",ascending=False)
    df_abitanti=df_abitanti[df_abitanti["anno"]==2019]



    # vettore con i bins limits
    thresholds=[]

    # andamento generale della popolazione ************************************
    plt.plot(np.arange(df_abitanti.shape[0]),df_abitanti["abitanti"])
    plt.title("Andamento generale abitanti per delegazione (ordianta da più a meno popolosa)")
    plt.show()



    #scelta degli outliers ********************************
    n,bins,patch=plt.hist(df_abitanti["abitanti"],bins=40, ec="black")
    plt.xticks(bins,rotation='vertical')
    outliers_limit=bins[11]
    plt.title("Scelta soglia per coorte Huge")
    plt.plot([outliers_limit,outliers_limit],[0,max(n)],color="red",linewidth=2)


    if save==True:
        plt.savefig("../plots/divisione coorti/metropoli.png")
    plt.show()
    thresholds.append(outliers_limit)




    # analisi normals **********************************
    normals=df_abitanti[df_abitanti["abitanti"]<outliers_limit]
    # andamento generale noramls
    plt.plot(np.arange(normals.shape[0]),normals["abitanti"])
    plt.title("Andameto genearle senza Huge")
    plt.show()

    n,bins,patch=plt.hist(normals["abitanti"],bins=10, ec="black")
    plt.xticks(bins,rotation='vertical')
    middle_limit=bins[3]
    plt.title("Scelta soglia per coorte big(destra della linea)")
    plt.plot([middle_limit,middle_limit],[0,max(n)],color="red",linewidth=2)
    if save==True:
        plt.savefig("../plots/divisione coorti/grandi.png")
    plt.show()
    thresholds.append(middle_limit)





    # analisi middle **********************************
    middle=df_abitanti[df_abitanti["abitanti"]<middle_limit]
    # andamento generale noramls
    plt.plot(np.arange(middle.shape[0]),middle["abitanti"])
    plt.title("Andamento generale coorte Middle")
    plt.show()

    n,bins,patch=plt.hist(middle["abitanti"],bins=30, ec="black")
    plt.xticks(bins,rotation='vertical')
    little_limit=bins[1]
    plt.title("Scrematura little")
    plt.plot([little_limit,little_limit],[0,max(n)],color="red",linewidth=2)
    if save==True:
        plt.savefig("../plots/divisione coorti/piccole (medie).png")
    plt.show()

    #si vede che le zone piccole hanno una rappresentanza maggiore e le si separano
    thresholds.append(little_limit)




    # seconda analisi middle_tolti i piccoli
    middle=middle[middle["abitanti"]>=little_limit]
    plt.title("Andamento generale middle")
    plt.plot(np.arange(middle.shape[0]),middle["abitanti"])
    plt.show()

    n,bins,patch=plt.hist(middle["abitanti"],bins=9, ec="black")
    plt.xticks(bins,rotation='vertical')
    plt.title("Scelta soglie per sottoclassi di middle")
    plt.plot([bins[3],bins[3]],[0,max(n)],color="red",linewidth=2)
    plt.plot([bins[6],bins[6]],[0,max(n)],color="red",linewidth=2)
    if save==True:
        plt.savefig("../plots/divisione coorti/sottoclassi medie.png")
    plt.show()

    thresholds_short=np.array(sorted(thresholds))

    thresholds.insert(2,bins[3])
    thresholds.insert(3,bins[6])
    thresholds=sorted(thresholds)
    thresholds


    # little
    little=df_abitanti[df_abitanti["abitanti"]<little_limit]




    # composozione finale dei df
    # manca da specificare la popolazione  associata
    middle_1=middle[middle["abitanti"]<thresholds[1]]

    middle_2=middle[middle["abitanti"]>=thresholds[1]]
    middle_2=middle_2[middle_2["abitanti"]<thresholds[2]]

    middle_3=middle[middle["abitanti"]>=thresholds[2]]

    #middle globale

    middle=middle_1.copy(deep=True)
    middle=middle.append(middle_2)
    middle=middle.append(middle_3)


    big=normals[normals["abitanti"]>=thresholds[3]]

    huge=df_abitanti[df_abitanti["abitanti"]>=thresholds[4]]

    all_no_little=df_abitanti[df_abitanti["abitanti"]>=thresholds[0]]



    #stampa info
    print("Little")
    print("Soglia 0-"+str(thresholds[0]))
    print("Delegazioni: "+str(little.shape[0])+"     "+str(100*little.shape[0]/df_abitanti.shape[0])+" %")
    print("Popolazione: "+str(sum(little["abitanti"]))+"    "+str(100*sum(little["abitanti"])/sum(df_abitanti["abitanti"]))+" %\n\n\n\n")

    print("Middle 1")
    print("Soglia "+str(thresholds[0])+"-"+str(thresholds[1]))
    print("Delegazioni: "+str(middle_1.shape[0])+"     "+str(100*middle_1.shape[0]/df_abitanti.shape[0])+" %")
    print("Popolazione: "+str(sum(middle_1["abitanti"]))+"    "+str(100*sum(middle_1["abitanti"])/sum(df_abitanti["abitanti"]))+" %\n\n\n\n")

    print("Middle 2")
    print("Soglia "+str(thresholds[1])+"-"+str(thresholds[2]))
    print("Delegazioni: "+str(middle_2.shape[0])+"     "+str(100*middle_2.shape[0]/df_abitanti.shape[0])+" %")
    print("Popolazione: "+str(sum(middle_2["abitanti"]))+"    "+str(100*sum(middle_2["abitanti"])/sum(df_abitanti["abitanti"]))+" %\n\n\n\n")

    print("Middle 3")
    print("Soglia "+str(thresholds[2])+"-"+str(thresholds[3]))
    print("Delegazioni: "+str(middle_3.shape[0])+"     "+str(100*middle_3.shape[0]/df_abitanti.shape[0])+" %")
    print("Popolazione: "+str(sum(middle_3["abitanti"]))+"    "+str(100*sum(middle_3["abitanti"])/sum(df_abitanti["abitanti"]))+" %\n\n\n\n")

    print("Middle aggregato")
    print("Soglia "+str(thresholds[0])+"-"+str(thresholds[3]))
    print("Delegazioni: "+str(middle.shape[0])+"     "+str(100*middle.shape[0]/df_abitanti.shape[0])+" %")
    print("Popolazione: "+str(sum(middle["abitanti"]))+"    "+str(100*sum(middle["abitanti"])/sum(df_abitanti["abitanti"]))+" %\n\n\n\n")

    print("Big")
    print("Soglia "+str(thresholds[3])+"-"+str(thresholds[4]))
    print("Delegazioni: "+str(big.shape[0])+"     "+str(100*big.shape[0]/df_abitanti.shape[0])+" %")
    print("Popolazione: "+str(sum(big["abitanti"]))+"    "+str(100*sum(big["abitanti"])/sum(df_abitanti["abitanti"]))+" %\n\n\n\n")

    print("Huge")
    print("Soglia "+str(thresholds[4])+"-"+str(max(huge["abitanti"])))
    print("Delegazioni: "+str(huge.shape[0])+"     "+str(100*huge.shape[0]/df_abitanti.shape[0])+" %")
    print("Popolazione: "+str(sum(huge["abitanti"]))+"    "+str(100*sum(huge["abitanti"])/sum(df_abitanti["abitanti"]))+" %\n\n\n\n")




    #RICALCOLO TI TUTTI I DF PER COMPRENDERE LE ANNATE PRECEDENTI (df in sede di df_abitanti)

    # little
    little=df[df["abitanti"]<little_limit]

    middle=df[df["abitanti"]<middle_limit]
    middle=middle[middle["abitanti"]>=little_limit]

    # composozione finale dei df
    # manca da specificare la popolazione  associata
    middle_1=middle[middle["abitanti"]<thresholds[1]]

    middle_2=middle[middle["abitanti"]>=thresholds[1]]
    middle_2=middle_2[middle_2["abitanti"]<thresholds[2]]

    middle_3=middle[middle["abitanti"]>=thresholds[2]]


    normals=df[df["abitanti"]<outliers_limit]

    big=normals[normals["abitanti"]>=thresholds[3]]

    huge=df[df["abitanti"]>=thresholds[4]]

    all_no_little=df[df["abitanti"]>=thresholds[0]]


    #middle globale

    middle=middle_1.copy(deep=True)
    middle=middle.append(middle_2)
    middle=middle.append(middle_3)


    return df,little,middle_1,middle_2,middle_3,middle,big,huge, all_no_little,thresholds,thresholds_short

df,little,middle_1,middle_2,middle_3,middle,big,huge,all_no_little,thresholds,thresholds_short=make_all_df(True)


middle.shape[0]+little.shape[0]+big.shape[0]+huge.shape[0]
df.shape[0]
