from __future__ import division
from fnvhash import fnv0_32
from murmur2 import murmur64a
import math
import pandas
import time

start_time = time.time()
m = 104998095
bit_vector = [0] * m
n = 0

chunksize = 1000000

for chunk in pandas.read_csv('data.csv', chunksize=chunksize):

    for query in chunk['Query']:

        query = str(query)
        fnvhash_query = fnv0_32(query) % m
        murmur_query = murmur64a(query, len(query), 9111) % m

        bit_vector[fnvhash_query] += 1
        bit_vector[murmur_query] += 1
        n+=1

end_time = time.time()

print("\nBloom filter executed in %s seconds." % (end_time - start_time))

print "\nEnter `exit` to exit\nEnter `stats` to see benchmark\nEnter `query [your_string]` to check if query exists or not\nEnter `add [your_string]` to append to bloom filter"

try:

    while 1:

        checker = str(raw_input('\n>>> '))

        if checker == '0' or checker == 'exit':
            print "\nTerminating Program...\n"
            print "Good-bye, cruel world!\n"
            break

        elif checker == 'stats' or checker == '1':

            k = (m//n)*math.log(2,math.e)
            print '\nIdeal value of k =', str(k)
            print '\nProbability of error:',str((1 - math.e**(-2*n/m))**2)

        elif checker == 'swag':print "\nThis program was brought to you by Koishore Roy. :)"

        else:

            slug = checker.split(' ')

            if slug[0] == 'query':

                shell_query = ' '.join(slug[1:])
                fnvhash_shell_query = fnv0_32(shell_query) % m
                murmur_shell_query = murmur64a(shell_query, len(shell_query), 9111) % m

                if bit_vector[fnvhash_shell_query] or bit_vector[murmur_shell_query]:
                    print '\nTrue', str(min(bit_vector[fnvhash_shell_query], bit_vector[murmur_shell_query]))
                else:
                    print '\nFalse',

            elif slug[0] == 'add':

                shell_query = ' '.join(slug[1:])

                fnvhash_shell_query = fnv0_32(shell_query) % m
                murmur_shell_query = murmur64a(shell_query, len(shell_query), 9111) % m

                bit_vector[fnvhash_shell_query] += 1
                bit_vector[murmur_shell_query] += 1

            else:
                print "\nEnter valid command!"

except KeyboardInterrupt:

    print "\nTerminating Program...\n"
    print "Good-bye, cruel world!\n"
