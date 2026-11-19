import pandas as pd
import seaborn as sns
import matplotlib as plt
import numpy as np
sysbook = pd.read_csv(r"C:\Users\Admin\Desktop\20261117--DE5M5\data\03_Library Systembook.csv")

syscust = pd.read_csv(r"data\03_Library SystemCustomers.csv")


def na_clean (df) :
    df = df.dropna()
    return df
''' reusuable - allows for function/code to be reused for exampole'''

def title_corrector (series) :
    seriestitled = series.str.title()
    return seriestitled

def remove_formating (df) :
    df_clean = df.replace('"', "",regex= True)
    return df_clean

def date_corrector (series) :
    seriestitled = pd.to_datetime(series,dayfirst=True,errors="coerce" ) 
    return seriestitled

def datediff (s1, s2) :
 series_diff = s2 - s1
 return series_diff

def ok_books(df):
 df = df[df["datediff"] > pd.Timedelta(0)]
 return df

syscust = na_clean(syscust)
sysbook = na_clean(sysbook)
sysbook = remove_formating(sysbook)
sysbook["Books"] = title_corrector(sysbook["Books"]) 
sysbook["Book checkout"] = date_corrector(sysbook["Book checkout"])
sysbook["Book Returned"] = date_corrector(sysbook["Book Returned"])
sysbook["datediff"] = datediff(sysbook["Book checkout"],sysbook["Book Returned"])
sysbook = ok_books(sysbook)

sysbook.to_csv(r"C:\Users\Admin\Desktop\20261117--DE5M5\day_4_final_task\data\03_Library Systembook_clean_3.csv", index=False)

syscust.to_csv(r"C:\Users\Admin\Desktop\20261117--DE5M5\day_4_final_task\data\03_Library Systemcust_clean_3.csv", index=False)