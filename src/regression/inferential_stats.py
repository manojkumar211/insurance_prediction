import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import df
from scipy import stats
from statsmodels.stats.weightstats import ztest



# By applying Shapiro, we can able to identify the normality of the data/column.


class data_shapiro:

    age_shapiro=stats.shapiro(df['age'])
    bmi_shapiro=stats.shapiro(df['bmi'])
    expenses_shapiro=stats.shapiro(df['expenses'])

    def __init__(self,age_shapiro,bmi_shapiro,expenses_shapiro):

        self.age_shapiro=age_shapiro
        self.bmi_shapiro=bmi_shapiro
        self.expenses_shapiro=expenses_shapiro

    def age_column_shapiro(self):
        return self.age_shapiro
    def bmi_column_shapiro(self):
        return self.bmi_shapiro
    def expenses_column_shapiro(self):
        return self.expenses_shapiro

    
""" Data is normal """


age_ztest=ztest(df['age'],value=df['age'].quantile(0.95),alternative="two-sided",ddof=0) # type: ignore

