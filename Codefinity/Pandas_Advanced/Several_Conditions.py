import pandas as pd
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/planet', index_col = 0)
data_extracted = data.loc[(data['est_diameter_min'] > 3.5) & (data['hazardous'] == True)]
print(data_extracted)

# Exercise:

import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/planet', index_col = 0)

# Extract data
data_extracted = data.loc[(data['absolute_magnitude'] >= 25) & (data['hazardous'] == False)]

# Output data
print(data_extracted.sample(5))