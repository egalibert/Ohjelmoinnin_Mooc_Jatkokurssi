import pandas as pd
import numpy as np

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/update/ds_salaries_statistics', index_col = 0)

# Calculate the standard deviation using the function from the NumPy library
std_1 = np.std(df['salary_in_usd'])
# Calculate the standard deviation using the function from the pandas library
std_2 = df['salary_in_usd'].std()

print('The standard deviation using NumPy library is', round(std_1, 2))
print('The standard deviation using pandas library is', round(std_2, 2))