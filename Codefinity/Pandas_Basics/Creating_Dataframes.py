import pandas as pd
dataset = {'country' : ['Thailand', 'Philippines', 'Monaco', 'Malta', 'Sweden', 'Paraguay', 'Latvia'],
          'continent' : ['Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'South America', 'Europe'],
          'capital':['Bangkok', 'Manila', 'Monaco', 'Valletta', 'Stockholm', 'Asuncion', 'Riga']}
countries = pd.DataFrame(dataset)

countries['population'] = [61399000, 75967000, 39244, 380200, 10380491, 5496000, 2424200]
print(countries)