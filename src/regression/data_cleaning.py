import numpy as np
import pandas as pd
from data import df


# Renaming the sex column into as gender column.

df.rename(columns={'sex':'gender'},inplace=True)
print(df.head())