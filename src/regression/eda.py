import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import df


continuous_variables=['bmi','expenses']
discrete_count=['age','children']
discrete_categorical=['gender','smoker','region']



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
    age_18_40=df[(df['age']>=18) & (df['age']<40) & (df['expenses']>13270)][['age','expenses']].count()
    age_40_50=df[(df['age']>=40) & (df['age']<50) & (df['expenses']>13270)][['age','expenses']].count()
    age_50_60=df[(df['age']>=50) & (df['age']<60) & (df['expenses']>13270)][['age','expenses']].count()
    age_60_70=df[(df['age']>=60) & (df['age']<70) & (df['expenses']>13270)][['age','expenses']].count()


    def __init__(self,age_shape,age_min,age_max,age_describe,age_nullvalue,age_skew,age_std,age_var,age_zeros,
                 age_unique,age_corr_output,age_18_40,age_40_50,age_50_60,age_60_70):
        
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
        self.age_18_40=age_18_40
        self.age_40_50=age_40_50
        self.age_50_60=age_50_60
        self.age_60_70=age_60_70
        
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
    
    def age_column_18_40(self):
        return self.age_18_40
    
    def age_column_40_50(self):
        return self.age_40_50
    
    def age_column_50_60(self):
        return self.age_50_60
    
    def age_column_60_70(self):
        return self.age_60_70
    
    

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


sns.pairplot(data=df,vars=continuous_variables,hue='gender') # type: ignore
plt.title("Age column's pair plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/pairplots/age_pair.png")


fig,ax=plt.subplots(figsize=(5,5))
sns.heatmap(data=df[['age','expenses']].corr(),cmap='tab20',annot=True,ax=ax)
plt.title("Age column's heatmap plot")
plt.savefig("E:/NareshiTech/insurance_prediction/visual_plots/heatmap/age_heatmap.png")




class eda_gender:

    gender_unique=df['gender'].unique().tolist()
    gender_values=df['gender'].value_counts()
    gender_smoker=pd.crosstab(df['gender'],df['smoker'],margins=True)
    gender_nullvalue=df['gender'].isnull().sum()
    gender_female_smok=df[(df['gender']=='female') & (df['smoker']=='yes')][['gender','smoker']].count()
    gender_female_nosmok=df[(df['gender']=='female') & (df['smoker']=='no')][['gender','smoker']].count()
    gender_male_smok=df[(df['gender']=='male') & (df['smoker']=='yes')][['gender','smoker']].count()
    gender_male_nosmok=df[(df['gender']=='male') & (df['smoker']=='no')][['gender','smoker']].count()
    gender_female_smok_exp=df[(df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)][['gender','expenses']].count()
    gender_female_nosmok_exp=df[(df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)][['gender','expenses']].count()
    gender_male_smok_exp=df[(df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)][['gender','expenses']].count()
    gender_male_nosmok_exp=df[(df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)][['gender','expenses']].count()
    gender_female_chil0_exp=df[(df['gender']=='female') & (df['children']==0) & (df['expenses']>13270)][['gender','expenses']].count()
    gender_female_chil1_exp=df[(df['gender']=='female') & (df['children']==1) & (df['expenses']>13270)][['gender','expenses']].count()
    gender_female_chil2_exp=df[(df['gender']=='female') & (df['children']==2) & (df['expenses']>13270)][['gender','expenses']].count()
    gender_female_chil3_exp=df[(df['gender']=='female') & (df['children']==3) & (df['expenses']>13270)][['gender','expenses']].count()
    gender_female_chil4_exp=df[(df['gender']=='female') & (df['children']==4) & (df['expenses']>13270)][['gender','expenses']].count()
    gender_female_chil5_exp=df[(df['gender']=='female') & (df['children']==5) & (df['expenses']>13270)][['gender','expenses']].count()
    gender_male_chil0_exp=df[(df['gender']=='male') & (df['children']==0) & (df['expenses']>13270)][['gender','expenses']].count()
    gender_male_chil1_exp=df[(df['gender']=='male') & (df['children']==1) & (df['expenses']>13270)][['gender','expenses']].count()
    gender_male_chil2_exp=df[(df['gender']=='male') & (df['children']==2) & (df['expenses']>13270)][['gender','expenses']].count()
    gender_male_chil3_exp=df[(df['gender']=='male') & (df['children']==3) & (df['expenses']>13270)][['gender','expenses']].count()
    gender_male_chil4_exp=df[(df['gender']=='male') & (df['children']==4) & (df['expenses']>13270)][['gender','expenses']].count()
    gender_male_chil5_exp=df[(df['gender']=='male') & (df['children']==5) & (df['expenses']>13270)][['gender','expenses']].count()


    def __init__(self,gender_unique,gender_values,gender_smoker,gender_nullvalue,gender_female_smok,gender_female_nosmok,
                 gender_male_smok,gender_male_nosmok,gender_female_smok_exp,gender_female_nosmok_exp,gender_male_smok_exp,
                 gender_male_nosmok_exp,gender_female_chil0_exp,gender_female_chil1_exp,gender_female_chil2_exp,gender_female_chil3_exp,
                 gender_female_chil4_exp,gender_female_chil5_exp,gender_male_chil0_exp,gender_male_chil1_exp,gender_male_chil2_exp,
                 gender_male_chil3_exp,gender_male_chil4_exp,gender_male_chil5_exp):
        
        self.gender_unique=gender_unique
        self.gender_values=gender_values
        self.gender_smoker=gender_smoker
        self.gender_nullvalue=gender_nullvalue
        self.gender_female_smok=gender_female_smok
        self.gender_female_nosmok=gender_female_nosmok
        self.gender_male_smok=gender_male_smok
        self.gender_male_nosmok=gender_male_nosmok
        self.gender_female_smok_exp=gender_female_smok_exp
        self.gender_female_nosmok_exp=gender_female_nosmok_exp
        self.gender_male_smok_exp=gender_male_smok_exp
        self.gender_male_nosmok_exp=gender_male_nosmok_exp
        self.gender_female_chil0_exp=gender_female_chil0_exp
        self.gender_female_chil1_exp=gender_female_chil1_exp
        self.gender_female_chil2_exp=gender_female_chil2_exp
        self.gender_female_chil3_exp=gender_female_chil3_exp
        self.gender_female_chil4_exp=gender_female_chil4_exp
        self.gender_female_chil5_exp=gender_female_chil5_exp
        self.gender_male_chil0_exp=gender_male_chil0_exp
        self.gender_male_chil1_exp=gender_male_chil1_exp
        self.gender_male_chil2_exp=gender_male_chil2_exp
        self.gender_male_chil3_exp=gender_male_chil3_exp
        self.gender_male_chil4_exp=gender_male_chil4_exp
        self.gender_male_chil5_exp=gender_male_chil5_exp

    def gender_column_unique(self):
        return self.gender_unique
    def gender_column_values(self):
        return self.gender_values
    def gender_column_smoker(self):
        return self.gender_smoker
    def gender_column_nullvalue(self):
        return self.gender_nullvalue
    def gender_column_female_smok(self):
        return self.gender_female_smok
    def gender_column_female_nosmok(self):
        return self.gender_female_nosmok
    def gender_column_male_smok(self):
        return self.gender_male_smok
    def gender_column_male_nosmok(self):
        return self.gender_male_nosmok
    def gender_column_female_smok_exp(self):
        return self.gender_female_smok_exp
    def gender_column_female_nosmok_exp(self):
        return self.gender_female_nosmok_exp
    def gender_column_male_smok_exp(self):
        return self.gender_male_smok_exp
    def gender_column_male_nosmok_exp(self):
        return self.gender_male_nosmok_exp
    def gender_column_female_chil0_exp(self):
        return self.gender_female_chil0_exp
    def gender_column_female_chil1_exp(self):
        return self.gender_female_chil1_exp
    def gender_column_female_chil2_exp(self):
        return self.gender_female_chil2_exp
    def gender_column_female_chil3_exp(self):
        return self.gender_female_chil3_exp
    def gender_column_female_chil4_exp(self):
        return self.gender_female_chil4_exp
    def gender_column_female_chil5_exp(self):
        return self.gender_female_chil5_exp
    def gender_column_male_chil0_exp(self):
        return self.gender_male_chil0_exp
    def gender_column_male_chil1_exp(self):
        return self.gender_male_chil1_exp
    def gender_column_male_chil2_exp(self):
        return self.gender_male_chil2_exp
    def gender_column_male_chil3_exp(self):
        return self.gender_male_chil3_exp
    def gender_column_male_chil4_exp(self):
        return self.gender_male_chil4_exp
    def gender_column_male_chil5_exp(self):
        return self.gender_male_chil5_exp
    


