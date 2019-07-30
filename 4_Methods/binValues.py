from pandas import cut, value_counts

primnums = [2, 3, 5, 7, 11, 13, 17, 19,
            23, 29, 31, 37, 41, 43, 47]
numbins = [0, 10, 20, 30, 40, 50]
catg = cut(primnums, numbins)
print catg
print '---'
print value_counts(catg)
print '- auto categorize -'
# precision store/display
catg = cut(primnums, 3, precision=1)
print value_counts(catg)
