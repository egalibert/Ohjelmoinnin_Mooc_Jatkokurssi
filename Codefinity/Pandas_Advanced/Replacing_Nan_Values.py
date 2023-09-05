import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic_2', index_col = 0)

# Replace missing values with the mean
data['Age'].fillna(value=data['Age'].mean(), inplace=True)
# Calculate the sum of missing values
NaN = data['Age'].isna().sum()

print(NaN)