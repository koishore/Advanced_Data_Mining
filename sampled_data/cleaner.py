import csv
import sys

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

def nullify(string):

    if string == '':
        return 'null'

    if string == '\n':
        return 'null'

    if '\n' in string:
        return string.replace('\n','')

    return string

with open('cleaned_data.csv', 'w') as csvfile:
    fieldnames = ['AnonID', 'Query', 'QueryTime', 'ItemRank', 'ClickURL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

for count in xrange(10):

    with open('user-ct-test-collection-' + str(count+1).zfill(2) + '.txt') as ifile:
        f = ifile.readlines()

    for i in xrange(1,len(f)):

        temp = map(nullify, f[i].split('\t'))


        with open('cleaned_data.csv', 'a') as csvfile:

            fieldnames = ['AnonID', 'Query', 'QueryTime', 'ItemRank', 'ClickURL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                            {
                                'AnonID': temp[0],
                                'Query': temp[1],
                                'QueryTime': temp[2],
                                'ItemRank': temp[3],
                                'ClickURL': temp[4],
                            }
                            )
        status = 'Working on user-ct-test-collection-' + str(count+1).zfill(2) + '.txt line number ' + str(i) + ' of ' + str(len(f))
        progress(i, len(f), status)
