import matplotlib.pyplot as plt
from seaborn import pairplot, load_dataset

# Load example tips dataset
iris = load_dataset('iris')
print iris.head()
print iris.tail()
print iris.describe()

fig =pairplot(data=iris, hue='species')

plt.savefig('snsPplot.png', bbox_inches='tight', dpi=70)