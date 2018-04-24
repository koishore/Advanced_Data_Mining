import random
from random import randint
import pandas as pd
import csv

dict = {}
n=100 # no of variables
path="C:/Users/admin/Desktop/"
file="cleaned_data.csv"
p = pd.read_csv(path+file)

for i in range(0,len(p)):
	h = (p.iloc[i]['Query'])
	if str(h) in dict: 
		dict[str(h)]=dict[str(h)]+1
	else:
		r=randint(0, i)
		if r<n: 
			if len(dict)!=n:
				dict[str(h)]=1
			if len(dict)==n:
				for key in random.sample(dict.keys(), 1):
					del dict[key]
				dict[str(h)]=1

print(dict)
print(((sum(dict.values())*2)-len(dict))*(len(p)/len(dict)))
