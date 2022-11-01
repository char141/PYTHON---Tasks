my_list = list()
filename = input("Enter file: ")
fhand = open(filename)
for line in fhand:
   # print(line)
    words = line.split()
    # print(words)
    for word in words:
        if word in my_list:
            continue
        my_list.append(word)
print(sorted(my_list))
