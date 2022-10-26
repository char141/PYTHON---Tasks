filename = input('Enter a file name: ')
fhandle = open(filename)
for line in fhandle:
    fout = line.rstrip().upper()
print(fout)
