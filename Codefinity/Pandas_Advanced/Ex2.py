import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/cars', index_col = 0)

fuel_types = ['Plug-in Hybrid', 'Hybrid']
# Put the condition on the column 'Price'
condition_1 = data['Price'].between(15000, 20000, inclusive = 'left')
# Put the condition on the column 'Year'
condition_2 = data['Year'].between(2015, 2020, inclusive = 'neither')
# Put the condition on the column 'Fuel_type'
condition_3 = data['Fuel_type'].isin(fuel_types)

# Unite three conditions
data_extracted = data.loc[condition_1 & condition_2 & condition_3]

print(data_extracted.head())