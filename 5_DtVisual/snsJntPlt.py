import matplotlib.pyplot as plt
from seaborn import jointplot, load_dataset

# Load example tips dataset
iris = load_dataset('iris')
print iris.head()
print iris.tail()
print iris.describe()

fig = jointplot(x='sepal_length', y='petal_length',
          data=iris)

plt.savefig('snsJntPlt.png', bbox_inches='tight', dpi=70)
