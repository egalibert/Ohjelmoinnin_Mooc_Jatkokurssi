# Import library
import numpy as np
import pandas as pd

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/update/ds_salaries_statistics', index_col = 0)

# Calculate the mean value
mean = np.mean(df['salary_in_usd'])
# Calculate the median value
median = np.median(df['salary_in_usd'])

print('The mean value is', mean)
print('The median value is', median)