import random
import sys

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))

def nullify(string):

    if string == '':
        return 'null'

    if string == '\n':
        return 'null'

    if '\n' in string:
        return string.replace('\n','')

    return string

for count in range(10):
    with open ('user-ct-test-collection-' + str(count + 1).zfill(2) + '.txt') as ifile:
        f = ifile.readlines()

    list_of_random_numbers = []
    for i in range(10000):

        flag = True
        while flag:
            random_index = random.randint(1, len(f))

            if random_index not in list_of_random_numbers:
                list_of_random_numbers.append(random_index)
                flag = False

            else:
                continue

    list_of_random_numbers = sorted(list_of_random_numbers)
    
    writer = open('sampled_data/user-ct-test-collection-' + str(count + 1).zfill(2) + '.txt', 'w')
    writer.write(f[0])

    for i in range(len(list_of_random_numbers)):
        writer.write(f[list_of_random_numbers[i]])
        status = 'Writing to user-ct-test-collection-' + str(count+1).zfill(2) + '.txt line number ' + str(i) + ' of ' + str(len(list_of_random_numbers))
        progress(i, len(list_of_random_numbers), status)
    writer.close()
