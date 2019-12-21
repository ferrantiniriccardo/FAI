import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import copy





def csv_to_list(csv_f):
    data_list=[]
    with open(csv_f) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            data_list.append(row)
    return data_list


def get_title(data_list):
    return data_list[0][0]


def get_colnames(data_list):
    colnames=copy.deepcopy(data_list[2])
    colnames[0]=data_list[1][0]
    colnames=[string.upper() for string in colnames]
    colnames[21]=data_list[1][21]
    colnames[22]=data_list[1][22]
    colnames[-1]=data_list[1][-1]
    colnames=[string.replace("/","-") for string in colnames]
    colnames.append("REGIONE")
    return colnames

def remove_title_colnames(data_list):
    data_list=data_list[:-3]
    return data_list[3:]



def fix_character(data_list):
    new_data_list=[]
    for row in data_list:
        first=row[0]
        row=row[1:]
        row=[i.replace(".","") for i in row]
        row=[i.replace("€","") for i in row]
        row=[i.replace("%","") for i in row]
        row=[i.replace(",",".") for i in row]
        row=[i.replace(" ","") for i in  row]
        row=[i.replace("-","") for i in  row]
        row.insert(0,first)
        new_data_list.append(row)
    return(new_data_list)


def rem_add_region(data_list):
    new_data_list=[]
    regioni=["abruzzo","basilicata","calabria","campania","emilia romagna","friuli venezia giulia" ,"lazio","liguria","lombardia","marche","molise","piemonte","puglia","sardegna","sicilia","toscana","trentino alto adige","umbria","valle d'aosta","veneto"]

    current=""
    for row in data_list:
        if row[0].lower() in regioni:
            current=row[0]
        else:
            row.append(current)
            new_data_list.append(row)
    return new_data_list

def fix_missing_value(data_list):
    new_data_list=[]
    for row in data_list:
        row=["0" if i=="" else i for i in row]
        new_data_list.append(row)
    return new_data_list

def add_popolazione(df):
    popolazione=pd.read_csv("fai_popolazione_province.csv")
    popolazione=(popolazione['Popolazione provincia'].values).astype(int)
    df['POPOLAZIONE']=popolazione
    return df

def make_df(csv_fai):
    data_list=csv_to_list(csv_fai)
    title=get_title(data_list)
    colnames=get_colnames(data_list)
    colnames
    data_list=remove_title_colnames(data_list)
    data_list=fix_character(data_list)
    data_list=rem_add_region(data_list)
    data_list=fix_missing_value(data_list)
    df=pd.DataFrame(data_list,columns=colnames)
    df=add_popolazione(df)

    return df



def make_dict(df):
    pop_dict=dict(zip(df['DELEGAZIONE/GRUPPO'].values,np.zeros(len(df['DELEGAZIONE/GRUPPO'].values)).astype(int)))
    df_province=pd.read_csv("province.csv")



    province_lower=[]
    for prov in df_province['Provincia'].values:
        province_lower.append(prov.lower())

    popolazione=[]
    for val in df_province['Popolazione'].values:
        popolazione.append(int(val.replace(".","")))

    province_dict=dict(zip(province_lower,popolazione))

    province_dict

    for key in pop_dict:
        for key_prov in province_dict:
            if key_prov in key.lower():
                pop_dict[key]=province_dict[key_prov]

    return pop_dict
