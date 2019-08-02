from numpy import random, abs, sign
from pandas import DataFrame

df = DataFrame(random.randn(300, 6))
# print '- Head -'
# print df.head()
# print '- tail -'
# print df.tail()
print '- description -'
print df.describe()

# One of more coord. with value > 3
print '- Condition on DataFrame -'
print df[(abs(df) > 3).any(1)]

# Substitution values with condition
print '- Substitute for sign*5 -'
df[abs(df) > 3] = sign(df)*5
print df.describe()
