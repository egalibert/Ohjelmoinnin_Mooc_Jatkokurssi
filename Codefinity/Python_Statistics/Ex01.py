import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import scipy.stats as st
import numpy as np

# Read csv file
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/section_1/confidence.csv', index_col = 0)

# Output the first five observations
first_five = data.head(5)
print(first_five)

# Create the histplot
plot = sns.histplot(data = data,
                  x = 'body_mass_g',
                 kde = True)
plot.set_title('Penguins')
plot.set(xlabel = 'The Mass', ylabel = 'The Quantity')
plt.show()