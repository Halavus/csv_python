# py2

import sys
import csv
import CSVConverter
from NumUpdate import Do as upd

'''
in cell 3(py) is zu haende
in cell 6(py) is land
in cell 10(py) is tel
'''

# TODO learn writer ?

#filename = sys.argv[1]
filename = 'DPD.csv'

f = open(filename, 'rb')
cr = csv.reader(f, delimiter=';', quotechar=None)

csv = CSVConverter.CSV(filename)

def curLine(ln_number):
    return csv.csv[ln_number]

def zuHaende(ln):
    if curLine(ln)[3] != '':
        return True
    else:
        return False

def firma(ln):
    if curLine(ln)[1] != '' and curLine(ln)[2] == '' and curLine(ln)[3] == '':
        return False
    else:
        return True


