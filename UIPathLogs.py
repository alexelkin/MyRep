

infile = 'c:/work/uipath/raw-logs.csv'
outfile = 'c:/work/uipath/final-logs.csv'
MIN_LEN = 109


with open(outfile, "w") as out:

    with open(infile, "r") as f:
        for line in f:
            line = line.strip()
            print('Source: ', line.strip())
            if len(line) > MIN_LEN and not line.startswith('""'):
#                print('Accepted', line[0:2] )
                if not line[0:2] == 'Id':
                    line = line[:len(line)-3]
                out.write( line + '\n')



