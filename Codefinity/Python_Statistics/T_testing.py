import pandas as pd
import scipy.stats as st

# Load the data
male = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/Testing2.0/male.csv').squeeze()
female = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/Testing2.0/female.csv').squeeze()

# Apply t-test
t_stat, pvalue = st.ttest_ind(male, female, equal_var=True, alternative="greater")

if pvalue > 0.05:
# Check if we should support or not the null hypothesis if pvalue > 0.05:
    print("We support the null hypothesis, the mean values are equal")
else:
    print("We reject the null hypothesis, males are taller")