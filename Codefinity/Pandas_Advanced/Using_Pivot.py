import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/plane', index_col = 0)

# The code using .groupby()
data_flights_1 = data[['Length', 'Flight']].groupby('Flight').mean()
# The same code using .groupby()
data_flights_2 = data[['Length', 'Flight']].groupby('Flight').agg('mean')

# The same code using .pivot_table()
data_flights_3 = pd.pivot_table(data, values = 'Length',
                      index = 'Flight',
                      aggfunc = 'mean')

print(data_flights_1.head())