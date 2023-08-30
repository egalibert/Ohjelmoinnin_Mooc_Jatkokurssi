import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/IMDb_Data_final.csv', index_col = 0)

# Extract needed rows and columns
data_extracted = data.iloc[:50, [1, 4]]

print(data_extracted.head())