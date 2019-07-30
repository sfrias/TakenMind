from numpy import arange
from pandas import DataFrame

df = DataFrame(
    arange(25).reshape(5, 5),
    index=['UBER', 'OLA', 'GRAB', 'GOJEK', 'LYFT'],
    columns=['RE', 'LO', 'QU', 'GR', 'AG'])
# RE is Revenue     LO is Loss      QU is quality
# GR is genre       AG is age
print df
# Change index values with updating df in place
print '- Change idx updating df in place -'
df.rename(index=str.title, columns=str.lower,
          inplace=True)
print df
# change indexes using mapping
print'- Change indexes using mapping -'
df.index = df.index.map(str.lower)
df.columns = df.columns.map(str.upper)
# df.index[= columns(str.upper)
print df
# Renaming with dictionary
print '- Renaming with dictionary -'
df.rename(index={'uber': 'U', 'ola': 'O', 'grab': 'G',
                 'lyft': 'L'},
          columns={'RE': 'Revenue'}, inplace=True)
print df
