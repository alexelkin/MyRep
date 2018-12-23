def slices(s, *args):

    print( 'S = ', s )
    print('In slices, arg = ', *args )
    position = 0
    for length in args:
        print('Length is ', length)
        yield s[position:position + length]
        position += length


fields = [2, 3, 4, 5, 6, 7]
original = 'abcdefghijklmnopqrstuvwxyz0123456789'

#parse_string( string, *fields )
result = list(slices(original, *fields))
print( result )

# if __name__ == "__main__":
#     parse_string(original, fields)