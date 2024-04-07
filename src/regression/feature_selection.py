import numpy as np
import pandas as pd
from data_cleaning import ds
import statsmodels.formula.api as smf
from data_wrangling import X,y
import sklearn
from sklearn.model_selection import train_test_split


print(ds.head())
ols_method=smf.ols(formula="y~X",data=ds).fit()
print(ols_method.summary())


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=True)

