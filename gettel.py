import CSVConverter as c

f=c.CSV('DPD.csv')

def gettel(line):
    return f.line(line)[10]
