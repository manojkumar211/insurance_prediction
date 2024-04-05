# Data:-
```
- Data is related to insurance. whether person will take insurance or not based on some parameters.
- Input variables are ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
- Output variable is ['expenses']

```

## shape of the data:-
```
- In this data, we are having total Rows-1338 and Columns-7.
- In Columns, 2 columns are continuous variables, 2 are discrete_count variables and 3 are discrete_categorical variables.
- We are having 1 duplicate value in this data.
- There is no any Null values in our data set.

"We are having unique values by columns wise"

age           47
sex            2
bmi          275
children       6
smoker         2
region         4
expenses    1337

```

# EDA:-

## Age column:-
```
count    1338.000000
mean       39.207025
std        14.049960
min        18.000000
25%        27.000000
50%        39.000000
75%        51.000000
max        64.000000

- There is no any Null values in Age column.
- The Age column having 0.05567251565299186 skewness which means it almost zero, nothing but the Age column is symmetrical distributed.
- The Age column's Standard deviation value is 14.044709038954522.
- The Age column's Variance value is 197.2538519888909
- There is no zeros are present in the Age column.
- Thers are 47 unique values in the Age column.
- The Age column is correlated 29% of the time with the Expenses column.
- There is no Outliers are present in the Age column.
- Total 181 persons can take insurance in Age between 18 to 39.
- Total 78 persons can take insurance in Age between 40 to 49.
- Total 74 persons can take insurance in Age between 50 to 59.
- Total 87 persons can take insurance in Age between 60 to 70.
- Might be total 420 members are ready to take insurance instead of 1338, which means 918 members are not ready to take insurance based on Age group.

```

## Gender column:-
```
- In Gender column, we have female and male unique values.
['female', 'male']

male      676
female    662

- Total males are 676 and females are 662. the two categories are equally destributed the data. so, there is no any
inbalanced data, which means we are having balanced data.

- There is no any Null values are in Gender column.
- Total 115 female smokers are here in our data.
- Total 547 female non-smokers are here in our data.
- Total 159 male smokers are here in our data.
- Total 517 male non-smokers are here in our data.
- 115 female smokers are taken insurance.
- 84 female non-smokers are taken insurance.
- 158 male smokers are taken insurance.
- 63 male non-smokers are taken insurance.
- In female or male, Who those are having less children those people are taking insurance.

```