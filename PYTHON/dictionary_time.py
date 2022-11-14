lst = list()
dictionary_time = dict()
fname = input("Enter the file name: ")
try:
    fhandle = open(fname)
except FileNotFoundError:
    print("File not found")
    exit()

for line in fhandle:
    words = line.split()
    if len(words) < 2 or words[0] != "From":
        continue
    colon_position = words[5].find(":")
    hour = words[5][:colon_position]
    if hour not in dictionary_time:
        dictionary_time[hour] = 1
    else:
        dictionary_time[hour] += 1

for key, val in list(dictionary_time.items()):
    lst.append((key, val))
lst.sort()
for key, val in lst:
    print(key, val)
