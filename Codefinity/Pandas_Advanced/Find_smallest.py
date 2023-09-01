import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/cars', index_col = 0)

# To retrieve specific values of the column 'Year'
data_extracted = data.loc[data['Year'] > 2010]
# Extract the `15` cheapest cars
data_cheapest = data_extracted.nsmallest(15, 'Price',
                                keep = 'all')

# Print data
print(data_cheapest)