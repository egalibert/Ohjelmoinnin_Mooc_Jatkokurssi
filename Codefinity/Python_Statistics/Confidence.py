# Importing libraries
import scipy.stats as st
import numpy as np

confidence = 0

# Creating random normal distribution
dist = st.norm.rvs(size = 1000, loc = 50, scale = 2)

# Finding confidence interval
confidence = st.norm.interval(alpha=0.95, loc=np.mean(dist), scale=st.sem(dist))

print(confidence)