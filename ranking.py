import funzioni as fun
import coorti as coo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mlt
import os






def migliori(df_local,df_title,best_n,thresholds,save=False):
    """
        Barplot che riporta la classifica delle migliori n (best_n) e colora le barre in base alla cooorte
    """
    if save==True:
        try:
            os.mkdir("../plots/best")
        except OSError:
            pass

    dividendi=["tot_entrate","totale_n+r"]
    targets=["abitanti"]
    periodi=["GFA","GFP"]
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
                        df_to_plot=df_to_plot.iloc[:best_n]
                        colors,col_list,labels=fun.set_colors(df_to_plot,thresholds)
                        plt.bar((df_to_plot['delegazione'].values).astype(str),df_to_plot["target"],color=colors)
                        plt.title(dividendo+" su "+target+"  "+str(anno)+"  "+periodo+" "+df_title)
                        plt.xticks(rotation='vertical')
                        patch_list = [mpatches.Patch(color=col_list[i], label=labels[i]) for i in range(len(labels))]
                        plt.legend(handles=patch_list)
                        plt.gcf().subplots_adjust(bottom=0.50)
                        if save==True:
                            fig.savefig("../plots/best/"+dividendo+"/"+periodo+"/"+target+" "+str(anno)+" "+periodo+" "+df_title+".png")
                            plt.close()
                        else:
                            plt.show()


df,little,middle_1,middle_2,middle_3,middle,big,huge,all_no_little,thresholds,thresholds_short=coo.make_all_df()
migliori(all_no_little,"all dettaglio",50,thresholds,save=True)
