import pandas as pd
import numpy as np

dataset = {'animal': [np.NaN, 'Dog', np.NaN, 'Cat','Parrot', None],
'name': ['Dolly', None, 'Erin', 'Kelly', None, 'Odie']}
animal = pd.DataFrame(dataset)
# Find missing values
missing_value = animal.isna()
print(missing_value)