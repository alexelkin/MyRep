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
    reader = csv.reader(csvfile, delimiter='|', quotechar='"')
#    reader = csv.DictReader(csvfile, delimiter='|' )
    row_count = 0
    for row in reader:
#        print ('-'.join(row))
        print (row)
        i = 0
        newStr = ""
        for thing in row:
            if i != 0:
                newStr += ","
            newStr += thing.strip()
#            print( "appending " + thing.strip() + " to " + newStr )
#            print("{}: -{}-\n".format(i, thing.strip()))
            i+=1
        print("New: " + newStr);
        row_count += 1
    print( "Row " + str(row_count) )
#        print(row[0], row[1])


