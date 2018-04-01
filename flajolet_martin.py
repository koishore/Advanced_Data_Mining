import pandas as pd
import csv

p = pd.read_csv('/Users/salonibhogale/Documents/Advance Data Mining/Project/cleaned_data.csv')
max_nz = 0
for i in range(0,len(p)):
    h = hash(p.iloc[i]['Query'])
    b = "{0:b}".format(h)
    nz = len(b) - len(b.rstrip('0'))
    if nz > max_nz:
        max_nz = nz
        max_h = h


estimate = 2**max_nz

#use multiple hash functions

#split sample into groups --> Group Size ~ log(n); where n is the size of the universal set

#take average of groups

#take median of averages to arrive at closest possible answer 


