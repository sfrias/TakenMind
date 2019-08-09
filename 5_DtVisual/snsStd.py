# Changes for pycharm display_.py only this session

# Substitute 'from urllib.parse import urlencode'
# with 'from urllib import urlencode'

# Substitute 'from urllib.request import Request, urlopen'
# with 'from urllib2 import Request, urlopen'


# Comment:
# #from .supported_data_type import _standardize_value
import matplotlib.pyplot as plt
from seaborn import set, load_dataset,\
    boxplot, despine

set(style='ticks', palette='pastel')

# Load example tips dataset
tips = load_dataset('tips')
print tips.head()
print tips.tail()

# Draw a nested boxplot to show bills/day,time
fig = plt.figure(figsize=(4,4))

boxplot(x='day', y='total_bill', hue='smoker',
        palette=["m", "g"], data=tips)

despine(offset=10, trim=True)
plt.savefig('snsStd.png', bbox_inches='tight')
