# /bin/py2

import csv

# --------------------------------------------------

class CSV:
    '''This class puts the .csv file in a python list to access specific
    lines quickly with the appropriate method: line or cell.
    '''
    
    def __init__(self, filename):
        self.filename=filename
        
        f = open(filename, 'rb') 
        self.cr=csv.reader(f, delimiter=';', quotechar=None)
        
        lst=[]
        linecount=0
        for row in self.cr:
            lst.append(row)
            linecount += 1
        self.csv=lst

        self.linecount=linecount


    def line(self, y):

        if y <= self.linecount-1:
            line=self.csv[y]
            return line
        else:
            return False

    def cell(self, y, x):
        cell=self.csv[y][x]

        return cell

#    def lines(self, a=0, b=linecount-1):
#        '''Returns the lines in range a:b'''
#        for i in range(a, b):
#            print(self.line(i))


# --------------------------------------------------

def Return_values(csv_as_list, y, x=None):
    '''When the csv is put into a python list:
    y would be the line number
    x would be the cell number of that line
    '''

    if x == None:
        '''Returns one whole line.'''
        line = csv_as_list[y]
        return line

    else:
        cell = csv_as_list[y][x]
        return cell

# print '\n', filename, linecount, 'lines'
