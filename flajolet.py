import pandas as pd
import csv
import hashlib
import numpy as np
import mmh3
import csv

p1 = pd.read_csv('test1.csv',encoding='latin1')
p2 = pd.read_csv('test2.csv',encoding='latin1')
p3 = pd.read_csv('test3.csv',encoding='latin1')

p_fin = pd.concat([p1,p2,p3])

p_fin.to_csv('concat_3.csv',',')

max_nz1=0
max_nz2=0
max_nz3=0
for chunk in pd.read_csv('concat_3.csv',chunksize=500):
    for p in chunk['AnonID']:
        h1 = hash(p)
        b = "{0:b}".format(h1)
        nz = len(b) - len(b.rstrip('0'))
        if nz > max_nz1:
            max_nz1 = nz
        h2 = "{0:b}".format(mmh3.hash("{0:b}".format(p)))
        nz = len(h2)-len(h2.rstrip('0'))
        if nz>max_nz2:
            max_nz2=nz
        h3 = "{0:b}".format(int(hashlib.md5("{0:b}".format(p).encode(encoding='utf-8')).hexdigest(),16))
        nz = len(h3)-len(h3.rstrip('0'))
        if nz>max_nz3:
            max_nz3=nz


estimate1 = 2**max_nz1
estimate2 = 2**max_nz2
estimate3 = 2**max_nz3
print(estimate1,estimate2,estimate3)
print((estimate1+estimate2+estimate3)/3)

#split sample into groups --> Group Size ~ log(n); where n is the size of the universal set

#take average of groups

#take median of averages to arrive at closest possible answer

