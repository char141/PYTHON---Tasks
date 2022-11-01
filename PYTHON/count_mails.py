count = 0
fname = input("Enter a file name: ")
fhandle = open(fname)
for line in fhandle:
    if line.startswith("From"):
        count += 1
        words = line.split()
        print(words[1])
print('There were %d lines in the file with From as the first word' % count)
