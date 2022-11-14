import string

counts = 0
dictionary_counts = dict()
lst = list()
fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except FileNotFoundError:
    print("File not found!")
    exit()

for line in fhandle:
    line = line.translate(str.maketrans('','', string.digits))
    line = line.translate(str.maketrans('','', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            counts += 1
            if letter not in dictionary_counts:
                dictionary_counts[letter] = 1
            else:
                dictionary_counts[letter] += 1

for key, val in list(dictionary_counts.items()):
    lst.append((val / counts, key))

lst.sort(reverse=True)
for key, val in lst:
    print(key, val)
