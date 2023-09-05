import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic_0.csv')

# Calculate the number of missing values
Nan = data.isnull().sum()

# Output the result
print(Nan)