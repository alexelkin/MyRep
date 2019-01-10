import sys
import csv

delim = "|"

# path = 'C:/work/KPMG/20190108/Apdata_BSAK_01jan2017-15jan2017_QA.txt'
# outfile = 'C:/work/KPMG/20190108/Apdata_BSAK_01jan2017-15jan2017_QA.csv'

# path = 'C:/work/KPMG/20190108/Apdata_BSAS_01jan2017-15jan2017_QA.txt'
# outfile = 'C:/work/KPMG/20190108/Apdata_BSAS_01jan2017-15jan2017_QA.csv'

path = 'C:/work/KPMG/20190110/Apdata_BSIS_01jan2017-15jan2017_QA.txt'
outfile = 'C:/work/KPMG/20190110/Apdata_BSIS_01jan2017-15jan2017_QA.csv'

# path = 'C:/work/KPMG/20190110/Apdata_BSEG_01jan2017-15jan2017_QA_full.txt'
# outfile = 'C:/work/KPMG/20190110/Apdata_BSEG_01jan2017-15jan2017_QA_full.csv'



#with open('c:/temp/foo/file1.csv', 'rt') as csvfile:

# with open(path, 'rt') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')
#     for row in spamreader:
#         print (','.join(row))
#        print(row[" DocumentNo"], row[" Time    "])

#print('\n\nMow lets try disctionary\n')

with open(outfile, 'w') as fout:

    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=delim, quotechar='"')
        row_count = 0
        for row in reader:
#            print (row_count, row)
            if len(row) < 10:
                continue
            newStr = ""
            for thing in row:
                if len(newStr) != 0:
                    newStr += ","
                newStr += thing.strip()

            if len(newStr) < 2:
                continue
#            print("New: " + str(len(newStr)) + ": " + newStr)
            row_count += 1
#            print( "Row " + str(row_count) )
#             if row_count > 100:
#                 break
            fout.writelines(newStr)
            fout.write('\n')
