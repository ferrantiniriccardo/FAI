import funzioni as fun
import coorti as coo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mlt
import os






def migliori(df_local,df_title,best_n,thresholds,save=False):
    """
        Barplot che riporta la classifica delle migliori n in media (best_n) e colora le barre in base alla cooorte
    """
    if save==True:
        try:
            os.mkdir("../plots/best medie")
        except OSError:
            pass

    if len(thresholds)==5:
        colors_array=np.array(["black","green","yellow","red","blue","gray"])
        labels=["piccoli","medi_1","med1_2","medi_3","gandi","metropoli"]
        patch_list = [mpatches.Patch(color=colors_array[i], label=labels[i]) for i in range(len(colors_array))]

    else:
        colors_array=np.array(["black","green","yellow","red"])
        labels=["piccoli","medi","gandi","metropoli"]
        patch_list = [mpatches.Patch(color=colors_array[i], label=labels[i]) for i in range(len(colors_array))]


    dividendi=["tot_entrate","totale_n+r"]
    targets=["abitanti"]
    periodi=["GFA","GFP"]
    for dividendo in dividendi:
        if save==True:
            try:
                os.mkdir("../plots/best medie/"+dividendo)
            except OSError:
                pass

        for target in targets:
            fig=plt.figure()
            df_to_plot=df_local.copy(deep=True)
            df_to_plot["target"]=df_to_plot[dividendo]/df_to_plot[target]
            df_to_plot.sort_values(by="target",ascending=False,inplace=True)
            df_to_plot=df_to_plot.iloc[:best_n]
            colors=fun.set_colors(df_to_plot,thresholds)
            plt.bar((df_to_plot['delegazione'].values).astype(str),df_to_plot["target"],color=colors)
            plt.title(dividendo+" su "+target+"  "+df_title)
            plt.xticks(rotation='vertical')
            plt.legend(handles=patch_list)
            plt.gcf().subplots_adjust(bottom=0.50)
            if save==True:
                fig.savefig("../plots/best medie/"+dividendo+"/"+target+" "+df_title+".png")
                plt.close()
            else:
                plt.show()


df,little,middle_1,middle_2,middle_3,middle,big,huge,all_no_little,thresholds,thresholds_short=coo.make_all_df()
migliori(all_no_little,"all dettaglio",50,thresholds)

fun.cerca_delegazione("ancona",df)
ancona=df[df["delegazione"]=="Delegazione Ancona"]
ancona=ancona.append(df[df["delegazione"]=="Delegazione FAI Ancona"])
ancona

fun.cerca_delegazione("FAI",df)
