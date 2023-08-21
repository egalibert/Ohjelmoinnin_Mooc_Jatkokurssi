import pandas
dataset = {'country' : ['Thailand', 'Philippines', 'Monaco', 'Malta', 'Sweden', 'Paraguay', 'Latvia'], 'continent' : ['Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'South America', 'Europe'], 'capital':['Bangkok', 'Manila', 'Monaco', 'Valletta', 'Stockholm', 'Asuncion', 'Riga']}

countries = pandas.DataFrame(dataset)
# Accessing to the third and seventh rows
print(countries.iloc[2])
print(countries.iloc[6])