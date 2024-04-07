import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import df


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
    





class eda_bmi:

    bmi_describe=df['bmi'].describe()
    bmi_nullvalue=df['bmi'].isnull().sum()
    bmi_skew=df['bmi'].skew()
    bmi_corr=df[['bmi','expenses']].corr()
    bmi_low=df[df['bmi']<18.5]['bmi'].count()
    bmi_low_exp=df[(df['bmi']<18.5) & (df['expenses']>13270)]['bmi'].count()
    bmi_normal=df[(df['bmi']>=18.5) & (df['bmi']<25.0)]['bmi'].count()
    bmi_normal_exp=df[(df['bmi']>=18.5) & (df['bmi']<25.0) & (df['expenses']>13270)]['bmi'].count()
    bmi_high=df[(df['bmi']>=25.0) & (df['bmi']<30.0)]['bmi'].count()
    bmi_high_exp=df[(df['bmi']>=25.0) & (df['bmi']<30.0) & (df['expenses']>13270)]['bmi'].count()
    bmi_over=df[(df['bmi']>=30.0)]['bmi'].count()
    bmi_over_exp=df[(df['bmi']>=30.0) & (df['expenses']>13270)]['bmi'].count()

    def __init__(self,bmi_describe,bmi_nullvalue,bmi_skew,bmi_corr,bmi_low,bmi_low_exp,bmi_normal,bmi_normal_exp,
                 bmi_high,bmi_high_exp,bmi_over,bmi_over_exp):
        
        self.bmi_describe=bmi_describe
        self.bmi_nullvalue=bmi_nullvalue
        self.bmi_skew=bmi_skew
        self.bmi_corr=bmi_corr
        self.bmi_low=bmi_low
        self.bmi_low_exp=bmi_low_exp
        self.bmi_normal=bmi_normal
        self.bmi_normal_exp=bmi_normal_exp
        self.bmi_high=bmi_high
        self.bmi_high_exp=bmi_high_exp
        self.bmi_over=bmi_over
        self.bmi_over_exp=bmi_over_exp

    def bmi_column_describe(self):
        return self.bmi_describe
    def bmi_column_nullvalue(self):
        return self.bmi_nullvalue
    def bmi_column_skew(self):
        return self.bmi_skew
    def bmi_column_corr(self):
        return self.bmi_corr
    def bmi_column_low(self):
        return self.bmi_low
    def bmi_column_low_exp(self):
        return self.bmi_low_exp
    def bmi_column_normal(self):
        return self.bmi_normal
    def bmi_column_normal_exp(self):
        return self.bmi_normal_exp
    def bmi_column_high(self):
        return self.bmi_high
    def bmi_column_high_exp(self):
        return self.bmi_high_exp
    def bmi_column_over(self):
        return self.bmi_over
    def bmi_column_over_exp(self):
        return self.bmi_over_exp
    




class eda_children:

    df['children'].describe()
    df['children'].isnull().sum()
    df['children'].nunique()
    df['children'].skew()
    df[df['children']==0]['children'].count()
    df[df['children']==1]['children'].count()
    df[df['children']==2]['children'].count()
    df[df['children']==3]['children'].count()
    df[df['children']==4]['children'].count()
    df[df['children']==5]['children'].count()


    df[(df['children']==0) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==0) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==0) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==0) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==0) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==0) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==0) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==0) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    
    df[(df['children']==1) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==1) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==1) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==1) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==1) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==1) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==1) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==1) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()

    df[(df['children']==2) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==2) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==2) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==2) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==2) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==2) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==2) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==2) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()

    df[(df['children']==3) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==3) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==3) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==3) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==3) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==3) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==3) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==3) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()

    df[(df['children']==4) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==4) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==4) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==4) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==4) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==4) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==4) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==4) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()

    df[(df['children']==5) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==5) & (df['bmi']>=25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==5) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==5) & (df['bmi']<25.0) & (df['gender']=='female') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==5) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==5) & (df['bmi']>=25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==5) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='yes') & (df['expenses']>13270)]['children'].count()
    df[(df['children']==5) & (df['bmi']<25.0) & (df['gender']=='male') & (df['smoker']=='no') & (df['expenses']>13270)]['children'].count()






class eda_smoker:

    smoker_unique=df['smoker'].unique()
    smoker_value=df['smoker'].value_counts()
    smoker_nullvalue=df['smoker'].isnull().sum()
    smoker_female=df[(df['smoker']=='yes') & (df['gender']=='female')]['smoker'].count()
    smoker_no_female=df[(df['smoker']=='no') & (df['gender']=='female')]['smoker'].count()
    smoker_male=df[(df['smoker']=='yes') & (df['gender']=='male')]['smoker'].count()
    smoker_no_male=df[(df['smoker']=='no') & (df['gender']=='male')]['smoker'].count()


    def __init__(self,smoker_unique,smoker_value,smoker_nullvalue,smoker_female,smoker_no_female,smoker_male,smoker_no_male):

        self.smoker_unique=smoker_unique
        self.smoker_value=smoker_value
        self.smoker_nullvalue=smoker_nullvalue
        self.smoker_female=smoker_female
        self.smoker_no_female=smoker_no_female
        self.smoker_male=smoker_male
        self.smoker_no_male=smoker_no_male

    def smoker_column_unique(self):
        return self.smoker_unique
    def smoker_column_value(self):
        return self.smoker_value
    def smoker_column_nullvalue(self):
        return self.smoker_nullvalue
    def smoker_column_female(self):
        return self.smoker_female
    def smoker_column_no_female(self):
        return self.smoker_no_female
    def smoker_column_male(self):
        return self.smoker_male
    def smoker_column_no_male(self):
        return self.smoker_no_male
    




class eda_region:

    region_unique=df['region'].unique()
    region_value=df['region'].value_counts()
    region_sw_high=df[(df['region']=='southwest') & (df['expenses']>13270)]['region'].count()
    region_sw_low=df[(df['region']=='southwest') & (df['expenses']<13270)]['region'].count()
    region_se_high=df[(df['region']=='southeast') & (df['expenses']>13270)]['region'].count()
    region_se_low=df[(df['region']=='southeast') & (df['expenses']<13270)]['region'].count()
    region_nw_high=df[(df['region']=='northwest') & (df['expenses']>13270)]['region'].count()
    region_nw_low=df[(df['region']=='northwest') & (df['expenses']<13270)]['region'].count()
    region_ne_high=df[(df['region']=='northeast') & (df['expenses']>13270)]['region'].count()
    region_ne_low=df[(df['region']=='northeast') & (df['expenses']<13270)]['region'].count()

    def __init__(self,region_unique,region_value,region_sw_high,region_sw_low,region_se_high,region_se_low,region_nw_high,
                 region_nw_low,region_ne_high,region_ne_low):
        
        self.region_unique=region_unique
        self.region_value=region_value
        self.region_sw_high=region_sw_high
        self.region_sw_low=region_sw_low
        self.region_se_high=region_se_high
        self.region_se_low=region_se_low
        self.region_nw_high=region_nw_high
        self.region_nw_low=region_nw_low
        self.region_ne_high=region_ne_high
        self.region_ne_low=region_ne_low

    def region_column_unique(self):
        return self.region_unique
    def region_column_value(self):
        return self.region_value
    def region_column_sw_high(self):
        return self.region_sw_high
    def region_column_sw_low(self):
        return self.region_sw_low
    def region_column_se_high(self):
        return self.region_se_high
    def region_column_se_low(self):
        return self.region_se_low
    def region_column_nw_high(self):
        return self.region_nw_high
    def region_column_nw_low(self):
        return self.region_nw_low
    def region_column_ne_high(self):
        return self.region_ne_high
    def region_column_ne_low(self):
        return self.region_ne_low
    


class eda_expenses:

    expenses_describe=df['expenses'].describe()
    expenses_nullvalue=df['expenses'].isnull().sum()
    expenses_skew=df['expenses'].skew()
    expenses_female_high=df[(df['expenses']>13270) & (df['gender']=='female')]['expenses'].count()
    expenses_female_low=df[(df['expenses']<13270) & (df['gender']=='female')]['expenses'].count()
    expenses_male_high=df[(df['expenses']>13270) & (df['gender']=='male')]['expenses'].count()
    expenses_male_low=df[(df['expenses']<13270) & (df['gender']=='male')]['expenses'].count()

    def __init__(self,expenses_describe,expenses_nullvalue,expenses_skew,expenses_female_high,expenses_female_low,
                 expenses_male_high,expenses_male_low):
        
        self.expenses_describe=expenses_describe
        self.expenses_nullvalue=expenses_nullvalue
        self.expenses_skew=expenses_skew
        self.expenses_female_high=expenses_female_high
        self.expenses_female_low=expenses_female_low
        self.expenses_male_high=expenses_male_high
        self.expenses_male_low=expenses_male_low

    def expenses_column_describe(self):
        return self.expenses_describe
    def expenses_column_nullvalue(self):
        return self.expenses_nullvalue
    def expenses_column_skew(self):
        return self.expenses_skew
    def expenses_column_female_high(self):
        return self.expenses_female_high
    def expenses_column_female_low(self):
        return self.expenses_female_low
    def expenses_column_male_high(self):
        return self.expenses_male_high
    def expenses_column_male_low(self):
        return self.expenses_male_low
    
    




