import pandas as pd
import numpy as np

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/update/ds_salaries_statistics', index_col = 0)

# Calculate the variance using the function from the NumPy library
var_1 = np.var(df['salary_in_usd'])
# Calculate the variance using the function from the pandas library
var_2 = df['salary_in_usd'].var()

print('The variace using NumPy library is', var_1)
print('The variace using pandas library is', var_2)