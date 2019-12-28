import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
import os
import funzioni as fun


def make_all_df():

    df=pd.read_csv("dati/df_fai.csv", sep=",")
    df.columns=[i.lower() for i in df.columns]
    df.columns=[i if "/" not in i else i.replace("/","-") for i in df.columns]
    df.columns=[i if "€" not in i else i.replace("€","eur") for i in df.columns]
    df.columns=[i if "%" not in i else i.replace("%","perc") for i in df.columns]



    df_abitanti=df.copy(deep=True)

    df_abitanti=df_abitanti.sort_values(by="abitanti",ascending=False)
    df_abitanti=df_abitanti[df_abitanti["anno"]==2019]
    mlt.rcParams["figure.figsize"]=(20,10)
    mlt.rcParams["font.size"]=20



    # vettore con i bins limits
    thresholds=[]

    # andamento generale della popolazione ************************************
    plt.plot(np.arange(df_abitanti.shape[0]),df_abitanti["abitanti"])
    plt.show()



    #scelta degli outliers ********************************
    n,bins,patch=plt.hist(df_abitanti["abitanti"],bins=40)
    outliers_limit=bins[11]
    plt.plot([outliers_limit,outliers_limit],[0,max(n)],color="red",linewidth=2)
    plt.show()

    thresholds.append(outliers_limit)




    # analisi normals **********************************
    normals=df_abitanti[df_abitanti["abitanti"]<outliers_limit]
    # andamento generale noramls
    plt.plot(np.arange(normals.shape[0]),normals["abitanti"])
    plt.show()

    n,bins,patch=plt.hist(normals["abitanti"],bins=10)
    middle_limit=bins[3]
    plt.plot([middle_limit,middle_limit],[0,max(n)],color="red",linewidth=2)
    plt.show()
    thresholds.append(middle_limit)





    # analisi middle **********************************
    middle=df_abitanti[df_abitanti["abitanti"]<middle_limit]
    # andamento generale noramls
    plt.plot(np.arange(middle.shape[0]),middle["abitanti"])
    plt.show()

    n,bins,patch=plt.hist(middle["abitanti"],bins=30)
    little_limit=bins[1]
    plt.plot([little_limit,little_limit],[0,max(n)],color="red",linewidth=2)
    plt.show()

    #si vede che le zone piccole hanno una rappresentanza maggiore e le si separano
    thresholds.append(little_limit)




    # seconda analisi middle_tolti i piccoli
    middle=middle[middle["abitanti"]>=little_limit]
    plt.plot(np.arange(middle.shape[0]),middle["abitanti"])
    plt.show()

    n,bins,patch=plt.hist(middle["abitanti"],bins=9)
    plt.plot([bins[3],bins[3]],[0,max(n)],color="red",linewidth=2)
    plt.plot([bins[6],bins[6]],[0,max(n)],color="red",linewidth=2)
    plt.show()

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


    big=normals[normals["abitanti"]>=thresholds[3]]

    huge=df_abitanti[df_abitanti["abitanti"]>=thresholds[4]]

    all_no_little=df_abitanti[df_abitanti["abitanti"]>=thresholds[0]]

    return df,little,middle_1,middle_2,middle_3,big,huge, all_no_little,thresholds
