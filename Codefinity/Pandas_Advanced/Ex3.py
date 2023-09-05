import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/plane', index_col = 0)

# Create pivot table
data = pd.pivot_table(data, index = ['Airline', 'AirportFrom']
                     values = ['Delay', 'Length'],
                     aggfunc = {'Length': ['min', 'max'], 'Delay': 'count'})

print(data.head(10))