import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/cars', index_col = 0)

# Create a list
colors = ['Grey', 'White', 'Black']
# Extract needed values
data_extracted = data.loc[data['Color'].isin(colors)]

# Output data
print(data_extracted.tail(5))