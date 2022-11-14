#Program that categorizes each mail message by  the day of the week the commit was done and print then in a dictionary

dictionary_days = dict()
fname = input("Enter the file name: ")
try:
    fhandle = open(fname)
except FileNotFoundError :
    print("File cannot be opened ", fname)
    exit()
for line in fhandle:
    words = line.split()
    if len(words) < 3 or words[0] != "From":
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1
        else:
            dictionary_days[words[2]] += 1
print(dictionary_days)
