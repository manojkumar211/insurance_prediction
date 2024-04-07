import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import df
from data_cleaning import ds
from eda import continuous_variables


# Age Column:-

fig,ax=plt.subplots(figsize=(5,5))
sns.boxplot(data=df['age'],ax=ax) # type: ignore
plt.title("Age column's Box plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/age/age_box.png")

fig,ax=plt.subplots(figsize=(5,5))
sns.distplot(df['age'],ax=ax,label='skewness {}'.format(df['age'].skew())) # type: ignore
plt.title("Age column's dist plot")
plt.legend()
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/age/age_dist.png")

fig,ax=plt.subplots(figsize=(5,5))
sns.scatterplot(data=df,x='age',y='expenses')
plt.title("Age column's scatter plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/age/age_scatter.png")


sns.pairplot(data=df,vars=continuous_variables,hue='gender') # type: ignore
plt.title("Age column's pair plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/age/age_pair.png")


fig,ax=plt.subplots(figsize=(5,5))
sns.heatmap(data=df[['age','expenses']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Age column's heatmap plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/age/age_heatmap.png")


# Gender Column:-

fig,ax=plt.subplots(figsize=(5,5))
sns.barplot(data=df,x='gender',y='expenses',ax=ax)
plt.title("Gender Bar plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/gender/gender_bar.png")


fig,ax=plt.subplots(figsize=(5,5))
sns.countplot(data=df,x='gender',ax=ax)
plt.title("Gender count plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/gender/gender_count.png")

fig,ax=plt.subplots(figsize=(5,5))
plt.pie(df['gender'].value_counts(sort=False),labels=df['gender'].unique(),autopct="%0.03f%%")  # type: ignore
plt.legend()
plt.title("Pie chart for Gender in percentage")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/gender/gender_pie.png")


# BMI Column:-


fig,ax=plt.subplots(figsize=(5,5))
sns.boxplot(data=df['bmi'],ax=ax) # type: ignore
plt.title("BMI column's Box plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/bmi/bmi_box.png")

fig,ax=plt.subplots(figsize=(5,5))
sns.boxplot(data=ds['bmi'],ax=ax) # type: ignore
plt.title("BMI column's Box plot after Outliers")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/bmi/bmi_box1.png")

fig,ax=plt.subplots(figsize=(5,5))
sns.distplot(df['bmi'],ax=ax,label='skewness {}'.format(df['bmi'].skew())) # type: ignore
plt.title("bmi column's dist plot")
plt.legend()
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/bmi/bmi_dist.png")

fig,ax=plt.subplots(figsize=(5,5))
sns.scatterplot(data=df,x='bmi',y='expenses')
plt.title("bmi column's scatter plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/bmi/bmi_scatter.png")


fig,ax=plt.subplots(figsize=(5,5))
sns.heatmap(data=df[['bmi','expenses']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("bmi column's heatmap plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/bmi/bmi_heatmap.png")



# Children Column:-


fig,ax=plt.subplots(figsize=(5,5))
sns.barplot(data=df,x='children',y='expenses',ax=ax)
plt.title("children Bar plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/children/children_bar.png")


fig,ax=plt.subplots(figsize=(5,5))
sns.countplot(data=df,x='children',ax=ax)
plt.title("children count plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/children/children_count.png")


fig,ax=plt.subplots(figsize=(5,5))
plt.pie(df['children'].value_counts(sort=True),labels=df['children'].unique(),autopct="%0.03f%%") # type: ignore
plt.legend()
plt.title("Pie chart for children in percentage")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/children/children_pie.png")



# Smoker Column:-


fig,ax=plt.subplots(figsize=(5,5))
sns.barplot(data=df,x='smoker',y='expenses',ax=ax)
plt.title("smoker Bar plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/smoker/smoker_bar.png")


fig,ax=plt.subplots(figsize=(5,5))
sns.countplot(data=df,x='smoker',ax=ax)
plt.title("smoker count plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/smoker/smoker_count.png")

fig,ax=plt.subplots(figsize=(5,5))
plt.pie(df['smoker'].value_counts(sort=False),labels=df['smoker'].unique(),autopct="%0.3f%%",explode=[0,0.02])  # type: ignore
plt.legend()
plt.title("smoker Pie plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/smoker/smoker_pie.png")



# Region Column:-

fig,ax=plt.subplots(figsize=(5,5))
sns.barplot(data=df,x='region',y='expenses',ax=ax)
plt.title("region Bar plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/region/region_bar.png")


fig,ax=plt.subplots(figsize=(5,5))
sns.countplot(data=df,x='region',ax=ax)
plt.title("region count plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/region/region_count.png")

fig,ax=plt.subplots(figsize=(5,5))
plt.pie(df['region'].value_counts(sort=False),labels=df['region'].unique(),autopct="%0.3f%%")  # type: ignore
plt.legend()
plt.title("region Pie plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/region/region_pie.png")


# Expenses Column:-

fig,ax=plt.subplots(figsize=(5,5))
sns.boxplot(data=df['expenses'],ax=ax) # type: ignore
plt.title("expenses column's Box plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/expenses/expenses_box.png")

fig,ax=plt.subplots(figsize=(5,5))
sns.distplot(df['expenses'],ax=ax,label='skewness {}'.format(df['expenses'].skew())) # type: ignore
plt.title("expenses column's dist plot")
plt.legend()
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/expenses/expenses_dist.png")

fig,ax=plt.subplots(figsize=(5,5))
sns.scatterplot(data=df,x='expenses',y='expenses')
plt.title("expenses column's scatter plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/expenses/expenses_scatter.png")


fig,ax=plt.subplots(figsize=(10,5))
sns.heatmap(data=df[['age','bmi', 'children','expenses']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("expenses column's heatmap plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/expenses/expenses_heatmap.png")
