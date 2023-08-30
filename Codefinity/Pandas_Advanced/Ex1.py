import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/planet')

# Extract all rows from the column 'name' and 'hazardous'
data_extracted = data.iloc[:, ['name', 'hazardous']]

# Filter data
data_filtered = data_extracted.loc[data_extracted['hazardous'] == True]

# Output data set
print(data_filtered.head(5))