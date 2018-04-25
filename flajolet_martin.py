import pandas as pd
import csv
import hashlib
import mmh3
import math
import datetime

r = pd.read_csv('cleaned_data_partial.csv') #to compare accuracy with partial dataset
r_len=len(r)
#as total elements could be around 3crore, taking log(total-n) and making sure that the bit-length from hash function is
#at least log(total-n), setting lval to 32 (minimum 32 bits of binary array)
lval = 32
max_nz1=0
max_nz2=0
max_nz3=0
max_nz4=0
max_nz5=0
max_nz6=0
max_nz7=0
max_nz8=0
max_nz9=0
max_nz10=0

#for 10 hash functions
j = 0
print(datetime.datetime.now())
for chunk in pd.read_csv('cleaned_data.csv',chunksize=100000):
    for p in chunk['AnonID']:
        try:
            h1 = hash(p)
            b = "{0:b}".format(h1)
            if len(b) < lval:
                temp=''
                for i in range(0, lval-len(b)):
                    temp = temp + '0'
            b = temp+b
            nz = len(b) - len(b.rstrip('0'))
            if nz > max_nz1:
                max_nz1 = nz
            h2 = "{0:b}".format(mmh3.hash("{0:b}".format(p)))
            if len(h2) < lval:
                temp=''
                for i in range(0, lval-len(h2)):
                    temp = temp + '0'
            h2 = temp+h2
            nz = len(h2)-len(h2.rstrip('0'))
            if nz>max_nz2:
                max_nz2=nz
            h3 = "{0:b}".format(int(hashlib.md5("{0:b}".format(p).encode(encoding='utf-8')).hexdigest(),16))
            if len(h3) < lval:
                temp=''
                for i in range(0, lval-len(h3)):
                    temp = temp + '0'
            h3 = temp+h3
            nz = len(h3)-len(h3.rstrip('0'))
            if nz>max_nz3:
                max_nz3=nz
            h4 = "{0:b}".format(int(hashlib.sha224("{0:b}".format(p).encode(encoding='utf-8')).hexdigest(),16))
            if len(h4) < lval:
                temp=''
                for i in range(0, lval-len(h4)):
                    temp = temp + '0'
            h4 = temp+h4
            nz = len(h4)-len(h4.rstrip('0'))
            if nz>max_nz4:
                max_nz4=nz
            h5 = "{0:b}".format(int(hashlib.sha256("{0:b}".format(p).encode(encoding='utf-8')).hexdigest(),16))
            if len(h5) < lval:
                temp=''
                for i in range(0, lval-len(h5)):
                    temp = temp + '0'
            h5 = temp+h5
            nz = len(h5)-len(h5.rstrip('0'))
            if nz>max_nz5:
                max_nz5=nz
            h = "{0:b}".format(int(hashlib.sha1("{0:b}".format(p).encode(encoding='utf-8')).hexdigest(),16))
            if len(h) < lval:
                temp=''
                for i in range(0, lval-len(h)):
                    temp = temp + '0'
            h = temp+h
            nz = len(h)-len(h.rstrip('0'))
            if nz>max_nz6:
                max_nz6=nz
            h = "{0:b}".format(int(hashlib.blake2b("{0:b}".format(p).encode(encoding='utf-8')).hexdigest(),16))
            if len(h) < lval:
                temp=''
                for i in range(0, lval-len(h)):
                    temp = temp + '0'
            h = temp+h
            nz = len(h)-len(h.rstrip('0'))
            if nz>max_nz7:
                max_nz7=nz
            h = "{0:b}".format(int(hashlib.sha384("{0:b}".format(p).encode(encoding='utf-8')).hexdigest(),16))
            if len(h) < lval:
                temp=''
                for i in range(0, lval-len(h)):
                    temp = temp + '0'
            h = temp+h
            nz = len(h)-len(h.rstrip('0'))
            if nz>max_nz8:
                max_nz8=nz
            h = "{0:b}".format(int(hashlib.sha3_512("{0:b}".format(p).encode(encoding='utf-8')).hexdigest(),16))
            if len(h) < lval:
                temp=''
                for i in range(0, lval-len(h)):
                    temp = temp + '0'
            h = temp+h
            nz = len(h)-len(h.rstrip('0'))
            if nz>max_nz9:
                max_nz9=nz
            h = "{0:b}".format(int(hashlib.blake2s("{0:b}".format(p).encode(encoding='utf-8')).hexdigest(),16))
            if len(h) < lval:
                temp=''
                for i in range(0, lval-len(h)):
                    temp = temp + '0'
            h = temp+h
            nz = len(h)-len(h.rstrip('0'))
            if nz>max_nz10:
                max_nz10=nz
        except:
            print(p,"some kind of error")
            continue
    j = j+1
    print(j)
print(datetime.datetime.now())
R = (max_nz1 +max_nz2 +max_nz3 +max_nz4 +max_nz5 +max_nz6 +max_nz7 +max_nz8 +max_nz9 +max_nz10)/10
print("Average R",R)
print("Estimate:",2**R)

print(2**max_nz1,2**max_nz2,2**max_nz3,2**max_nz4,2**max_nz5,2**max_nz6,2**max_nz7,2**max_nz8,2**max_nz9,2**max_nz10)




#Using only 3 hash functions
max_nz1=0
max_nz2=0
max_nz3=0
print(datetime.datetime.now())
j = 0
lval = 32
for chunk in pd.read_csv('cleaned_data.csv',chunksize=100000):
    for p in chunk['AnonID']:
        try:
            h1 = hash(p)
            b = "{0:b}".format(h1)
            if len(b) < lval:
                temp=''
                for i in range(0, lval-len(b)):
                    temp = temp + '0'
            b = temp+b
            nz = len(b) - len(b.rstrip('0'))
            if nz > max_nz1:
                max_nz1 = nz
            h2 = "{0:b}".format(mmh3.hash("{0:b}".format(p)))
            if len(h2) < lval:
                temp=''
                for i in range(0, lval-len(h2)):
                    temp = temp + '0'
            h2 = temp+h2
            nz = len(h2)-len(h2.rstrip('0'))
            if nz>max_nz2:
                max_nz2=nz
            h3 = "{0:b}".format(int(hashlib.md5("{0:b}".format(p).encode(encoding='utf-8')).hexdigest(),16))
            if len(h3) < lval:
                temp=''
                for i in range(0, lval-len(h3)):
                    temp = temp + '0'
            h3 = temp+h3
            nz = len(h3)-len(h3.rstrip('0'))
            if nz>max_nz3:
                max_nz3=nz

        except:
            print(p,"some kind of error")
            continue
    j = j+1
    print(j)
print(datetime.datetime.now())
R = (max_nz1 +max_nz2 +max_nz3)/3
print("Average R",R)
print("Estimate:",2**R)
