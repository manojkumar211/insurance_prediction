# Data:-
```
- Data is related to insurance. whether person will take insurance or not based on some parameters.
- Input variables are ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
- Output variable is ['expenses']
- Total 420 members are spending more amount on medical expenses out of 1338.

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
- There are 47 unique values in the Age column.
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
- 115 female smokers are spending more amount on medical expenses.
- 84 female non-smokers are spending amount on more medical expenses.
- 158 male smokers are spending more amount on medical expenses.
- 63 male non-smokers are spending more amount on medical expenses.
- In female or male, Who those are having less children those people are spending more amount on medical expenses.

for calegorical plot:
we can apply 
- Pie plot
- Bar plot
- Count plot only.

```

## BMI:-
```
bmi range:
below 18.5 --- under weight
18.5 - 24.9 --- healthy weight
25.0 - 29.9 --- over weight
30.0 above --- obesity

count    1338.000000
mean       30.665471
std         6.098382
min        16.000000
25%        26.300000
50%        30.400000
75%        34.700000
max        53.100000

- There is no any Null values are present in this genger column.
- This BMI column having 0.28459296016731195 skewness. which is symmetrical distribution. but still we need to apply feature transformations to make normal.
- The BMI column is 0.19% correlated with expenses column.
- 20 members are suffering with low bmi. In this 20 members, only 4 members are spending more amount on medical expenses.
- 222 members are having good health. In this 222 members, only 68 members are spending more amount on medical expenses.
- 389 members are suffering with over weight issue. In this 389 members, only 111 members are spending more amount on medical expenses.
- 707 members are suffering with Obesity issue. In this 707 members, only 237 members are spending more amount on medical expenses.

- We find some outliers in BMI column.


```

## Children:-

```
count    1338.000000
mean        1.094918
std         1.205493
min         0.000000
25%         0.000000
50%         1.000000
75%         2.000000
max         5.000000

- We do not have any NUll values.
- In this column, we are having 6 unique values. Those values are [0,1,2,3,4,5]
- Children column having 0.9383804401702414 of skewness which is near to 1, mean it is considered as a skewed distribution.
- Children==0, having 574 records in our dataset.
- Children==1, having 324 records in our dataset.
- Children==2, having 240 records in our dataset.
- Children==3, having 157 records in our dataset.
- Children==4, having 25 records in our dataset.
- Children==5, having 18 records in our dataset.

- 41 members spending more amount on medical expenses in this parameters (Children==0, bmi>25, gender==female, smoker==yes).
- 29 members spending more amount on medical expenses in this parameters (Children==0, bmi>25, gender==female, smoker==no).
- 12 members spending more amount on medical expenses in this parameters (Children==0, bmi<25, gender==female, smoker==yes).
- 6 members spending more amount on medical expenses in this parameters (Children==0, bmi<25, gender==female, smoker==no).

- 51 members spending more amount on medical expenses in this parameters (Children==0, bmi>25, gender==male, smoker==yes).
- 27 members spending more amount on medical expenses in this parameters (Children==0, bmi>25, gender==male, smoker==no).
- 11 members spending more amount on medical expenses in this parameters (Children==0, bmi<25, gender==male, smoker==yes).
- 2 members spending more amount on medical expenses in this parameters (Children==0, bmi<25, gender==male, smoker==no).

- 19 members spending more amount on medical expenses in this parameters (Children==1, bmi>25, gender==female, smoker==yes).
- 11 members spending more amount on medical expenses in this parameters (Children==1, bmi>25, gender==female, smoker==no).
- 6 members spending more amount on medical expenses in this parameters (Children==1, bmi<25, gender==female, smoker==yes).
- 5 members spending more amount on medical expenses in this parameters (Children==1, bmi<25, gender==female, smoker==no).

- 34 members spending more amount on medical expenses in this parameters (Children==1, bmi>25, gender==male, smoker==yes).
- 9 members spending more amount on medical expenses in this parameters (Children==1, bmi>25, gender==male, smoker==no).
- 2 members spending more amount on medical expenses in this parameters (Children==1, bmi<25, gender==male, smoker==yes).
- 2 members spending more amount on medical expenses in this parameters (Children==1, bmi<25, gender==male, smoker==no).

- 14 members spending more amount on medical expenses in this parameters (Children==2, bmi>25, gender==female, smoker==yes).
- 13 members spending more amount on medical expenses in this parameters (Children==2, bmi>25, gender==female, smoker==no).
- 8 members spending more amount on medical expenses in this parameters (Children==2, bmi<25, gender==female, smoker==yes).
- 2 members spending more amount on medical expenses in this parameters (Children==2, bmi<25, gender==female, smoker==no).

- 27 members spending more amount on medical expenses in this parameters (Children==2, bmi>25, gender==male, smoker==yes).
- 12 members spending more amount on medical expenses in this parameters (Children==2, bmi>25, gender==male, smoker==no).
- 5 members spending more amount on medical expenses in this parameters (Children==2, bmi<25, gender==male, smoker==yes).
- 1 members spending more amount on medical expenses in this parameters (Children==2, bmi<25, gender==male, smoker==no).

- 9 members spending more amount on medical expenses in this parameters (Children==3, bmi>25, gender==female, smoker==yes).
- 14 members spending more amount on medical expenses in this parameters (Children==3, bmi>25, gender==female, smoker==no).
- 5 members spending more amount on medical expenses in this parameters (Children==3, bmi<25, gender==female, smoker==yes).
- 0 members spending more amount on medical expenses in this parameters (Children==3, bmi<25, gender==female, smoker==no).

- 21 members spending more amount on medical expenses in this parameters (Children==3, bmi>25, gender==male, smoker==yes).
- 7 members spending more amount on medical expenses in this parameters (Children==3, bmi>25, gender==male, smoker==no).
- 4 members spending more amount on medical expenses in this parameters (Children==3, bmi<25, gender==male, smoker==yes).
- 0 members spending more amount on medical expenses in this parameters (Children==3, bmi<25, gender==male, smoker==no).

- 0 members spending more amount on medical expenses in this parameters (Children==4, bmi>25, gender==female, smoker==yes).
- 4 members spending more amount on medical expenses in this parameters (Children==4, bmi>25, gender==female, smoker==no).
- 0 members spending more amount on medical expenses in this parameters (Children==4, bmi<25, gender==female, smoker==yes).
- 0 members spending more amount on medical expenses in this parameters (Children==4, bmi<25, gender==female, smoker==no).

- 3 members spending more amount on medical expenses in this parameters (Children==4, bmi>25, gender==male, smoker==yes).
- 2 members spending more amount on medical expenses in this parameters (Children==4, bmi>25, gender==male, smoker==no).
- 0 members spending more amount on medical expenses in this parameters (Children==4, bmi<25, gender==male, smoker==yes).
- 0 members spending more amount on medical expenses in this parameters (Children==4, bmi<25, gender==male, smoker==no).

- 0 members spending more amount on medical expenses in this parameters (Children==5, bmi>25, gender==female, smoker==yes).
- 0 members spending more amount on medical expenses in this parameters (Children==5, bmi>25, gender==female, smoker==no).
- 1 members spending more amount on medical expenses in this parameters (Children==5, bmi<25, gender==female, smoker==yes).
- 0 members spending more amount on medical expenses in this parameters (Children==5, bmi<25, gender==female, smoker==no).

- 0 members spending more amount on medical expenses in this parameters (Children==5, bmi>25, gender==male, smoker==yes).
- 1 members spending more amount on medical expenses in this parameters (Children==5, bmi>25, gender==male, smoker==no).
- 0 members spending more amount on medical expenses in this parameters (Children==5, bmi<25, gender==male, smoker==yes).
- 0 members spending more amount on medical expenses in this parameters (Children==5, bmi<25, gender==male, smoker==no).
```

## Smoker:
```
- In smoker column we are having 2 groups those are ['yes', 'no']
no     1064
yes     274

- There is no any Null values in this column.
- 115 female smoker are there in this dataset.
- 547 female non-smoker are there in this dataset.
- 159 male smokers are there in this dataset.
- 517 male non-smokers are there in this dataset.

```

## Region:-
```
- In Region column, we are having ['southwest', 'southeast', 'northwest', 'northeast'].

southeast    364
southwest    325
northwest    325
northeast    324

- In Region of southeast, 130 members are there spending more amount on medical expenses.
- In Region of southeast, 234 members are there spending less amount on medical expenses.

- In Region of southwest, 85 members are there spending more amount on medical expenses.
- In Region of southwest, 240 members are there spending less amount on medical expenses.

- In Region of northwest, 96 members are there spending more amount on medical expenses.
- In Region of northwest, 229 members are there spending less amount on medical expenses.

- In Region of northeast, 109 members are there spending more amount on medical expenses.
- In Region of northeast, 215 members are there spending less amount on medical expenses.
```

# Expenses:-
```
count     1338.000000
mean     13270.422414
std      12110.011240
min       1121.870000
25%       4740.287500
50%       9382.030000
75%      16639.915000
max      63770.430000

- There is no any Null values in this column.
- In Expenses column, we find 1.51587966289798 of skew. so, we need to apply feature transformation.
- We find more Outliers in this column.

- 199 Females are spending more amount on medical expenses.
- 463 Females are spending less amount on medical expenses.

- 221 Females are spending more amount on medical expenses.
- 455 Females are spending more amount on medical expenses.
```