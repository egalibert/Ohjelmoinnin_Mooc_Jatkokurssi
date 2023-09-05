import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic4.csv', index_col = 0)

# Rename the column
data.rename(columns = {'Fare' : 'Fare_fixed'}, inplace = True)
# Output the name of all columns
print(data.columns)