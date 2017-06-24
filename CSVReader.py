#! /usr/bin/python
# from a bash terminal
# 

import sys, csv

file = sys.argv[1]
x = int(sys.argv[2]) - 1

if len  (sys.argv) == 4:
    y = int(sys.argv[3]) - 1

f = open(file, 'rb') 
cr = csv.reader(f, delimiter=';', quotechar=None)

# line1 = cr.next()
# print line1[x]

lst = []
linecount = 0

for row in cr:
    lst.append(row)
    linecount += 1

if 'y' in locals():
    line = lst[x][y]
    print line
    print '-'*len(line), '\n', 'line number', x + 1, '|', 'cell number', y + 1
    print len(lst[x]), 'cells'

else:
    print lst[x]

print '\n', file, linecount, 'lines'
