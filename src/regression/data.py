import numpy as np
import pandas as pd


df=pd.read_csv("E:/NareshiTech/insurance_prediction/maindata/insurance.csv") # type: ignore



class data_information:
    
    data_head=df.head()
    data_tail=df.tail()
    data_descibe=df.describe()
    data_columns=df.columns.tolist()
    data_count=df.count()
    data_dtypes=df.dtypes
    data_shape=df.shape
    data_duplicates=df.duplicated().sum()
    data_info=df.info()
    data_nullvalue=df.isnull().sum()
    data_uniquevalue=df.nunique(axis=0)

    def __init__(self,data_head,data_tail,data_descibe,data_columns,data_count,data_dtypes,data_shape,data_duplicates,
                 data_info,data_nullvalue,data_uniquevalue):
        
        self.data_head=data_head
        self.data_tail=data_tail
        self.data_descibe=data_descibe
        self.data_columns=data_columns
        self.data_count=data_count
        self.data_dtypes=data_dtypes
        self.data_shape=data_shape
        self.data_duplicates=data_duplicates
        self.data_info=data_info
        self.data_nullvalue=data_nullvalue
        self.data_uniquevalue=data_uniquevalue

    def dataset_head_info(self):
        return self.data_head
    
    def dataset_tail_info(self):
        return self.data_tail
    
    def dataset_descibe_info(self):
        return self.data_descibe
    
    def dataset_columns_info(self):
        return self.data_columns
    
    def dataset_count_info(self):
        return self.data_count
    
    def dataset_dtypes_info(self):
        return self.data_dtypes
    
    def dataset_shape_info(self):
        return self.data_shape
    
    def dataset_duplicates_info(self):
        return self.data_duplicates
    
    def dataset_info_info(self):
        return self.data_info
    
    def dataset_nullvalue_info(self):
        return self.data_nullvalue
    
    def dataset_uniquevalue_info(self):
        return self.data_uniquevalue
    



