import sys, csv

data = csv.reader(open('train.csv'), delimiter=',')
next(data, None)
import operator

sortedlist = sorted(data, key=lambda row: int(row[2]), reverse=False)


def filterimg(line):
    if int(line[2]) <= 500:
        return True
    else:
        return False


filteredList = filter(filterimg, sortedlist)

with open("train_filter.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
    for line in filteredList:
        wr.writerow(line)
