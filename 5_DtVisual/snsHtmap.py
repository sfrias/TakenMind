from pandas import read_csv
from matplotlib.pyplot import subplots
from seaborn import heatmap, set
# Set link to download csv
csv = 'https://raw.githubusercontent.com/resbaz/' \
      'r-novice-gapminder-files/master/data/' \
      'gapminder-FiveYearData.csv'
# Load Dataframe from csv that's in link
df = read_csv(csv)
# Print Dataframe for test
print '- Printing Dataframe extracted from link -'
print df.head()
print '- Making a pivot table -'
dfpv = df.pivot_table(index='continent',
                      columns='year',
                      values='lifeExp',
                      aggfunc='mean')
# Print Pivot Table for test
print '- pivot table lifeExp for test -'
print dfpv
print dfpv.info()
# Generating Heat Map
print '- Generating heat map -'
set()
f, ax = subplots(figsize=(12,2))
heatmap(dfpv, annot=True, fmt='.0f', linewidths=.5, ax=ax)\
    .get_figure().\
    savefig('snsHtmap.png',
            bbox_inches='tight',
            dpi=80)
