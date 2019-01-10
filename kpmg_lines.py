import sys
import csv

delim = "|"

# path = 'C:/work/KPMG/20190108/Apdata_BSAK_01jan2017-15jan2017_QA.txt'
# outfile = 'C:/work/KPMG/20190108/Apdata_BSAK_01jan2017-15jan2017_QA.csv'

# path = 'C:/work/KPMG/20190108/Apdata_BSAS_01jan2017-15jan2017_QA.txt'
# outfile = 'C:/work/KPMG/20190108/Apdata_BSAS_01jan2017-15jan2017_QA.csv'

# path = 'C:/work/KPMG/20190108/Apdata_BSIK_01jan2017-15jan2017_QA.txt'
# outfile = 'C:/work/KPMG/20190108/Apdata_BSIK_01jan2017-15jan2017_QA.csv'

path = 'C:/work/KPMG/20190110/Apdata_BSEG_01jan2017-15jan2017_QA.txt'
outfile = 'C:/work/KPMG/20190110/Apdata_BSEG_01jan2017-15jan2017_QA_full.txt'



with open(outfile, 'w') as fout:

    with open(path) as csvfile:

        prev_line = ''

        for line in csvfile:
#            line = line.strip()
            line = line.replace('\r\n', '')
            line = line.replace('\n', '')

            if prev_line != '':
                prev_line = prev_line + line
                fout.write(prev_line + '\n')
                prev_line = ''
                continue
            if line[0] == '|':
#                print('Line starts')
                prev_line = line
                continue

