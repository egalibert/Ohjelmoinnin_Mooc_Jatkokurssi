import pandas as pd
import scipy.stats as st

home_workers = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/Testing2.0/work_from_home.csv').squeeze()
office_workers = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/Testing2.0/work_from_office.csv').squeeze()

# Apply t-test
tstat, pvalue = st.ttest_ind(home_workers, office_workers, equal_var= False, alternative='greater')

if pvalue > 0.05:
# Check if we should support or not the null hypothesis if p_test > 0.05:
    print('We support the null hypothesis, the mean values are equal')
else:
    print('We reject the null hypothesis, the mean values are different')