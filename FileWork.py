
fname = 'C:/work/git/MyRep/space_sep.txt'

with open(fname) as f:
    line = f.readlines()
    print( line )


with open(fname) as f:
    for line in f:
        print(line.strip())
        print( line.split())


