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
print '- Dropped duplicates keeping first, col1 -'
print df.drop_duplicates(['col1'], keep='first')
print '- Dropped duplicates keeping last, col1 -'
print df.drop_duplicates(['col1'], keep='last')

print'- Duplicated for col2 coincidence -'
print df.duplicated(['col2'])
print '- Dropped duplicates keeping first, col2 -'
print df.drop_duplicates(['col2'], keep='first')
print '- Dropped duplicates keeping last, col2 -'
print df.drop_duplicates(['col2'], keep='last')
