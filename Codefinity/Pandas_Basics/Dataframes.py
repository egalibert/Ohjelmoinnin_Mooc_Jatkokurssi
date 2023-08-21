import pandas as pd
dataset = {'name' : ['Ann', 'Alex', 'Kevin', 'Kate'], 
          'age' : [35, 12, 24, 45]}

data_frame = pd.DataFrame(dataset)
print(data_frame)