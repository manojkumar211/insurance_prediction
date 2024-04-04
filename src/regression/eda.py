import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import df


continuous_variables=df[['bmi','expenses']]
discrete_count=df[['age','children']]
discrete_categorical=df[['sex','smoker','region']]



class eda_age:

    age_shape=df['age'].shape
    age_min=df['age'].min()
    age_max=df['age'].max()
    age_describe=df['age'].describe()
    age_nullvalue=df['age'].isnull().sum()
    age_skew=df['age'].skew()
    age_std=df['age'].std(ddof=0)
    age_var=df['age'].var(ddof=0)
    age_zeros=df[df['age']==0]
    age_unique=len(df['age'].unique())
    age_corr_output=df[['age','expenses']].corr()

    def __init__(self,age_shape,age_min,age_max,age_describe,age_nullvalue,age_skew,age_std,age_var,age_zeros,
                 age_unique,age_corr_output):
        
        self.age_shape=age_shape
        self.age_min=age_min
        self.age_max=age_max
        self.age_describe=age_describe
        self.age_nullvalue=age_nullvalue
        self.age_skew=age_skew
        self.age_std=age_std
        self.age_var=age_var
        self.age_zeros=age_zeros
        self.age_unique=age_unique
        self.age_corr_output=age_corr_output

    def age_column_shape(self):
        return self.age_shape
    
    def age_column_min(self):
        return self.age_min
    
    def age_column_max(self):
        return self.age_max
    
    def age_column_describe(self):
        return self.age_describe
    
    def age_column_nullvalue(self):
        return self.age_nullvalue
    
    def age_column_skew(self):
        return self.age_skew
    
    def age_column_std(self):
        return self.age_std
    
    def age_column_var(self):
        return self.age_var
    
    def age_column_zeros(self):
        return self.age_zeros
    
    def age_column_unique(self):
        return self.age_unique
    
    def age_column_corr_output(self):
        return self.age_corr_output
    

fig,ax=plt.subplots(figsize=(5,5))
sns.boxplot(data=df['age'],ax=ax) # type: ignore
plt.title("Age column's Box plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/boxplots/age_box.png")

fig,ax=plt.subplots(figsize=(5,5))
sns.distplot(df['age'],ax=ax) # type: ignore
plt.title("Age column's dist plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/histoplots/age_dist.png")

fig,ax=plt.subplots(figsize=(5,5))
sns.scatterplot(data=df,x='age',y='expenses')
plt.title("Age column's scatter plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/scatterplots/age_scatter.png")


sns.pairplot(data=df,vars=continuous_variables,hue='sex') # type: ignore
plt.title("Age column's pair plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/pairplots/age_pair.png")


fig,ax=plt.subplots(figsize=(5,5))
sns.heatmap(data=df[['age','expenses']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Age column's heatmap plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/heatmap/age_heatmap.png")

