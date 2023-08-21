import pandas as pd
frame = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine.csv')

# Write your code below
# The first rows
first_lines = frame.head(10)
print(first_lines)
# The last rows
last_lines = frame.tail(15)
print(last_lines)
# Random rows
random_rows = frame.sample(12)
print(random_rows)