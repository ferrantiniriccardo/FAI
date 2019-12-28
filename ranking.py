import funzioni as fun
import coorti as coo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlt
import os


df,little,middle_1,middle_2,middle_3,big,huge,all_no_little,thresholds=coo.make_all_df()
df

migliori_2(all_no_little,"all",50,save=True)


def migliori_2(df_local_in,df_title,best,threshold=0,save=False):
    if save==True:
        try:
            os.mkdir("../plots/best")
        except OSError:
            pass

    dividendi=["tot_entrate","totale_n+r"]
    targets=["abitanti"]
    periodi=["GFA","GFP"]
    df_local=df_local_in.copy(deep=True)
    df_local=df_local[df_local["tot_entrate"]>threshold]
    for dividendo in dividendi:
        if save==True:
            try:
                os.mkdir("../plots/best/"+dividendo)
            except OSError:
                pass
        for periodo in periodi:
            if save==True:
                try:
                    os.mkdir("../plots/best/"+dividendo+"/"+periodo)
                except OSError:
                    pass
            for target in targets:
                for anno in np.unique(df_local["anno"].to_numpy()):
                    if anno!=2016:
                        fig=plt.figure()
                        df_to_plot=df_local[df_local["tipo"]==periodo]
                        df_to_plot=df_to_plot[df_to_plot["anno"]==anno]
                        df_to_plot["target"]=df_to_plot[dividendo]/df_to_plot[target]
                        df_to_plot.sort_values(by="target",ascending=False,inplace=True)
                        df_to_plot=df_to_plot.iloc[:best]
                        plt.bar((df_to_plot['delegazione'].values).astype(str),df_to_plot["target"])
                        plt.title(dividendo+" su "+target+"  "+str(anno)+"  "+periodo+" "+df_title)
                        plt.xticks(rotation='vertical')
                        plt.gcf().subplots_adjust(bottom=0.50)
                        if save==True:
                            fig.savefig("../plots/best/"+dividendo+"/"+periodo+"/"+target+" "+str(anno)+" "+periodo+".png")
                            plt.close()
                        else:
                            plt.show()
