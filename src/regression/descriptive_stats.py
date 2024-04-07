import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import df


# IQR Method:-

## IQR methon for Age column.

class iqr_bmi:

    q1_bmi=df['bmi'].quantile(0.25)
    q2_bmi=df['bmi'].quantile(0.50)
    q3_bmi=df['bmi'].quantile(0.75)

    iqr_bmi=q3_bmi-q1_bmi

    lower_bmi=q1_bmi-(1.5*iqr_bmi)

    upper_bmi=q3_bmi+(1.5*iqr_bmi)

    def __init__(self,q1_bmi,q2_bmi,q3_bmi,iqr_bmi,lower_bmi,upper_bmi):

        self.q1_bmi=q1_bmi
        self.q2_bmi=q2_bmi
        self.q3_bmi=q3_bmi
        self.iqr_bmi=iqr_bmi
        self.lower_bmi=lower_bmi
        self.upper_bmi=upper_bmi

    def q1_column_bmi(self):
        return self.q1_bmi
    def q2_column_bmi(self):
        return self.q2_bmi
    def q3_column_bmi(self):
        return self.q3_bmi
    def iqr_column_bmi(self):
        return self.iqr_bmi
    def lower_column_bmi(self):
        return self.lower_bmi
    def upper_column_bmi(self):
        return self.upper_bmi
    

## IQR methon for Expenses column.


class iqr_expenses:

    q1_expenses=df['expenses'].quantile(0.25)
    q2_expenses=df['expenses'].quantile(0.50)
    q3_expenses=df['expenses'].quantile(0.75)

    iqr_expenses=q3_expenses-q1_expenses

    lower_expenses=q1_expenses-(1.5*iqr_expenses)

    upper_expenses=q3_expenses+(1.5*iqr_expenses)

    def __init__(self,q1_expenses,q2_expenses,q3_expenses,iqr_expenses,lower_expenses,upper_expenses):

        self.q1_expenses=q1_expenses
        self.q2_expenses=q2_expenses
        self.q3_expenses=q3_expenses
        self.iqr_expenses=iqr_expenses
        self.lower_expenses=lower_expenses
        self.upper_expenses=upper_expenses

    def q1_column_expenses(self):
        return self.q1_expenses
    def q2_column_expenses(self):
        return self.q2_expenses
    def q3_column_expenses(self):
        return self.q3_expenses
    def iqr_column_expenses(self):
        return self.iqr_expenses
    def lower_column_expenses(self):
        return self.lower_expenses
    def upper_column_expenses(self):
        return self.upper_expenses
    
"""-----------------------------------------------------------------------------------------"""


# Skewness of data:-

class data_skewness:

    age_skewness=df['age'].skew()
    bmi_skewness=df['bmi'].skew()
    expenses_skewness=df['expenses'].skew()

    def __init__(self,age_skewness,bmi_skewness,expenses_skewness):

        self.age_skewness=age_skewness
        self.bmi_skewness=bmi_skewness
        self.expenses_skewness=expenses_skewness

    def age_column_skewness(self):
        return self.age_skewness
    def bmi_column_skewness(self):
        return self.bmi_skewness
    def expenses_column_skewness(self):
        return self.expenses_skewness
    




