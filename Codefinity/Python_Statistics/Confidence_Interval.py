import scipy.stats as st
import numpy as np

data = [104, 106, 106, 107, 107, 107, 108, 108, 108, 108, 108, 109, 109, 109, 110, 110, 111, 111, 112]
# Calculate the confidence interval
confidence = st.t.interval(alpha = 0.95,
                           df = len(data)-1,
                           loc = np.mean(data),
                           scale = st.sem(data))

print(confidence)