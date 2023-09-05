import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic3.csv', index_col = 0)

# Replace `-` with the `.`
data['Fare'] = data['Fare'].str.replace('-', '.')
# Convert column to the float type of data
data['Fare'] = data['Fare'].astype('float')

# Output the type of the column 'Fare'
print(data['Fare'].dtypes)