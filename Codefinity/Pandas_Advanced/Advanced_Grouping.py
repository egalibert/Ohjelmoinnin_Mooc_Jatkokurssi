import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/plane', index_col = 0)

# Group data
data_flights = data[['AirportFrom', 'Airline', 'Time', 'Length']].groupby(['AirportFrom', 'Airline']).apply(lambda x: (x['Length'] + x['Time']).min())

print(data_flights.head(10))