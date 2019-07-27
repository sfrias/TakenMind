from pandas import DataFrame

df = DataFrame({'col1':['uber', 'uber', 'grab', 'grab'],
                'col2': [5,4,4,2]})

print df

print '- Duplicated for all column coincidence -'
print df.duplicated()
print '- Dropped duplicates, all column -'
print df.drop_duplicates()


print'- Duplicated for col1 coincidence -'
print df.duplicated(['col1'])
print '- Dropped duplicates, col1 -'
print df.drop_duplicates(['col1'])

print'- Duplicated for col2 coincidence -'
print df.duplicated(['col2'])
print '- Dropped duplicates, col2 -'
print df.drop_duplicates(['col2'])