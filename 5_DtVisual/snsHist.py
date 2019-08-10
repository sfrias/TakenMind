#from numpy import
from numpy.random import randn
#from pandas import
from scipy import stats
from matplotlib.pyplot import hist,\
    savefig, show, figure
from seaborn import jointplot
ds0 = randn(1000)
ds1 = randn(1000)
print '--- ds1 head ---'
print ds1
ds2 = randn(300)
print '--- ds2 head ---'
print ds2

figure()
hist(ds1) # ten blocks by default

hist(ds2) # ten blocks by default
savefig('snsHist1.png', bbox_inches='tight',
        dpi=60)
figure()
hist(ds1, normed=True,bins=15,
     color='blue', alpha=0.50)
hist(ds2, normed=True,bins=15,
     color='green', alpha=0.50)
savefig('snsHist2.png', bbox_inches='tight',
        dpi=60)
figure()
plot = jointplot(ds0, ds1, kind='hex')
savefig('snsHist3.png',
                 bbox_inches='tight',
                 dpi=80)