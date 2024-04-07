import numpy as np
import pandas as pd
from data import df
from descriptive_stats import iqr_bmi


# Renaming the sex column into as gender column.

df.drop_duplicates(inplace=True,ignore_index=True)

ds=df.copy()

ds['gender'].replace({"female":0,"male":1},inplace=True)
ds['smoker'].replace({"no":0,"yes":1},inplace=True)
ds['region'].replace({"northeast":0,"northwest":1,"southeast":2,"southwest":3},inplace=True)


"""ds[(ds['bmi']<iqr_bmi.lower_bmi) | (ds['bmi']>iqr_bmi.upper_bmi)] # type: ignore
ds['bmi'].drop(index=[116, 286, 401, 543, 846, 859, 1046, 1087, 1316])
ds['bmi']=ds['bmi'].clip(lower=iqr_bmi.lower_bmi,upper=iqr_bmi.upper_bmi) # type: ignore
ds['bmi'][[116, 286, 401, 543, 846, 859, 1046, 1087, 1316]] # type: ignore
"""

