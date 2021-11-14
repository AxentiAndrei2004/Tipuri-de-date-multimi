import itertools
m={'A','B','C','D'}
for i in range(len(m)):
    submultime=itertools.combinations(m, i+1)
    print(set(submultime))