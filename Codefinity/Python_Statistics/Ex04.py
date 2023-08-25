import scipy.stats as st
import pandas as pd

before = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/Testing2.0/before.csv').squeeze()
after = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/Testing2.0/after.csv').squeeze()

stats, pvalue = st.ttest_rel(before, after, equal_var=False, alternative="two-sided")
# Check the null hypothesis
if pvalue > 0.05:
    print("We support the null hypothesis, the mean values are equal")
# Check the alternative hypothesis    
else:
    print("We reject the null hypothesis, the mean values are different")