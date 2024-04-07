import numpy as np
import pandas as pd
from data_cleaning import ds
from scipy.stats import boxcox


# Feature Transformation
# Feature Encoding
# Feature Scaling
# Discretization

"""
- No need to apply Feature Encoding, why because already applied replacements function.
- No need to apply Discretization, why because already applied some filter methods on data set.
- Age (0.0556), BMI (0.2845), Expenses (1.515) columns are having skewness. so, need to apply some Feature Transformation.
- No need to apply Feature Scaling, why because for regression model the scaling method will not show any effect.

"""

ds['expenses_boxcox'],param_exp=boxcox(ds['expenses']) # type: ignore
ds['bmi_boxcox'],param_bmi=boxcox(ds['bmi']) # type: ignore
ds['age_boxcox'],param_age=boxcox(ds['age']) # type: ignore

X=ds.iloc[:,[9,1,3,4,5,8]]
y=ds['expenses_boxcox']




