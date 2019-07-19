# Merging Datasets on columns.

import pandas as pd
import  numpy as np
from pandas import  Series, DataFrame

df1 = DataFrame({'reference': ['ola', 'uber', 'lyft', 'gojek', 'grab'],
                 'revenue': [1, 2, 3, 4, 5 ]})
df2 = DataFrame({'reference': ['ola', 'uber', 'uber', 'ola'],
                 'revenue': [1, 2, 3, 4 ]})
print df1
print '----------'
print df2
print '----------'
# Many to one  merging
# OMerge for the same index and reference
df0 = pd.merge(df1, df2)
print df0
# Merge for the same 'reference',and adds labels as different columns
df3 = pd.merge (df1, df2, on='reference', how='right')
print df3
# Merge for all the references, adding labels as different columns
df4 = pd.merge( df1, df2, on='reference', how='left')
print df4
# Merge union of references
df5 = pd.merge(df1,df2, on='reference', how='outer')
print df5


df6 = DataFrame({'reference': ['ola', 'ola', 'lyft', 'lyft', 'uber', 'uber', 'ola'],
                 'revenue': [1, 2, 3, 4, 5,6,7 ]})
df7 = DataFrame({'reference': ['uber', 'uber', 'lyft', 'ola', 'ola'],
                 'revenue': [1, 2, 3, 4, 5,]})
print '=========='
print df6
print df7
print pd.merge(df6,df7)
print '---inner-------'
print pd.merge(df6,df7, on='reference', how='inner')
print '----right------'
print pd.merge(df6,df7, on='reference', how='right')
print '-----left-----'
print pd.merge(df6,df7, on='reference', how='left')
print '------outer----'
print pd.merge(df6,df7, on='reference', how='outer')
print '=========='
# Multiple references
df8 = DataFrame({'reference': ['ola', 'ola', 'lyft' ],
                 'revenue': ['one', 'two', 'three' ],
                 'profit': [ 1, 2, 3 ]})
print df8

df9 = DataFrame({'reference': ['ola', 'ola', 'lyft', 'lyft'],
                 'revenue': ['one', 'one', 'one', 'three' ],
                 'profit': [ 4, 5, 6, 7 ]})
print df9
print '-----merge-------'
print pd.merge(df8, df9, on=['reference', 'revenue'],
               suffixes=('_df8', '_df9' ))
print '----inner------'
print pd.merge(df8, df9, on=['reference', 'revenue'], how='inner',
               suffixes=('_df8', '_df9' ))
print '---outer-------'
print pd.merge( df8, df9, on=['reference', 'revenue'], how='outer')
print '----left------'
print pd.merge(df8, df9, on=['reference', 'revenue'], how='left',
               suffixes=('_df8', '_df9' ))
print '-----right-----'
print pd.merge(df8, df9, on=['reference', 'revenue'], how='right',
               suffixes=('_df8', '_df9' ))

# Many to many merging