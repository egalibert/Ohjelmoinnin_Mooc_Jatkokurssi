import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/planet', index_col = 0)

# Write the first condition
condition_1 = data['est_diameter_min'] < 0.01
# Write the second condition
condition_2 = data['absolute_magnitude'] > 20
# Write the third condition
condition_3 = data['hazardous'] == False
# Write the general condition
data_extracted = data.loc[(condition_1 & condition_2) | condition_3]

print(data_extracted.head())