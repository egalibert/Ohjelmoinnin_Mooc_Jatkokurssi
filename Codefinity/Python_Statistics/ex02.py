import numpy as np
import scipy.stats as st
import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/section_1/mean_mass.csv')

# Extract the column 'mass'
mean_list = data['mass']

# Find the confidence interval
confidence = st.norm.interval(alpha = 0.95,
                 loc = np.mean(mean_list),
                 scale=st.sem(mean_list))