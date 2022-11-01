count = 0
dictionary_words = dict()
fname = input("Enter a filename: ")
fhandle = open(fname)
for line in fhandle:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:
            continue
        dictionary_words[word] = count

if 'programming' in dictionary_words:
    print("True")
else:
    print("False")
