import sys, csv
from collections import Counter

from more_itertools import take

data = csv.reader(open('train.csv'), delimiter=',')
next(data, None)
import operator

sortedlist = sorted(data, key=lambda row: int(row[2]), reverse=False)
counter = 0
label = -1
countmap = {}

def filterimg(el):
    if 50 <= int(el[1]) <= 100:
        return True
    else:
        return False


def filterclass(el):
    if str(el[2]) in top50dict:
        return True
    else:
        return False


for line in sortedlist:
    if int(line[2] != label):
        counter = 0
        label = line[2]
        countmap[line[2]] = 0
    else:
        countmap[line[2]] = countmap[line[2]] + 1

countmapsorted = dict(sorted(countmap.items(), key=operator.itemgetter(1), reverse=True))

filteredList = filter(filterimg, countmapsorted.items())
top50 = take(50, filteredList)
top50dict = dict(top50).keys()

with open("train_top50.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
    for line in top50:
        wr.writerow(line)

train_filter = filter(filterclass, sortedlist)

with open("train_filter.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
    for line in train_filter:
        wr.writerow(line)