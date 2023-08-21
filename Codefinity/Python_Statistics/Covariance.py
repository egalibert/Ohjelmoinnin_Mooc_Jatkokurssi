import pandas as pd 
import numpy as np

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/update/Stores.csv')

# Calculating covariance 
cov = np.cov(df['Store_Area'], df['Items_Available'])[0,1]

print(round(cov, 2))