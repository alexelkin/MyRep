import sys
import csv

path = 'C:/work/KPMG/20181214/delim.txt'

#with open('c:/temp/foo/file1.csv', 'rt') as csvfile:

# with open(path, 'rt') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')
#     for row in spamreader:
#         print (', '.join(row))
#         print(row[" DocumentNo"], row[" Time    "])




print('\n\nMow lets try disctionary\n')

with open(path) as csvfile:
#    reader = csv.reader(csvfile, delimiter='|', quotechar='"')
    reader = csv.DictReader(csvfile, delimiter='|', restkey = "NOKEY" )
    for row in reader:
        print( "Type: " + str(type(row)) )
        print (row)
        row_string = ""
        element_count = 0
        for element in row.values():
            if element_count != 0 :
                row_string += ","
            if element != None:
                row_string += str(element)
            element_count += 1
        print( "Row: " + row_string )
