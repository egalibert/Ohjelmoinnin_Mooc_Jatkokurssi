import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic3.csv', index_col = 0)

# Modify the column
data = pd.get_dummies(data, columns = ['Sex'])
# Calculate the sum of values
sex_male = data['Sex_male'].sum()
# Calculate the sum of values
sex_female = data['Sex_female'].sum()

# Output the sum
print(sex_male, sex_female)