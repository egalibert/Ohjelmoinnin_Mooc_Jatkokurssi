import pandas

dataset = {'country' : ['Thailand', 'Philippines', 'Monaco', 'Malta', 'Sweden', 'Paraguay', 'Latvia'],
          'continent' : [None, None, 'Europe', None, 'Europe', None, 'Europe'],
          'capital':['Bangkok', 'Manila', 'Monaco', 'Valletta', 'Stockholm', 'Asuncion', 'Riga']}
countries = pandas.DataFrame(dataset)
countries = countries.drop(columns = ['continent'],axis=1)
print(countries)