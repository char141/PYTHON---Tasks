import re

count = 0

exp = input("Enter a regular expression: ")
reg_exp = str(exp)

fname = "mbox-short.txt"
fhandle = open(fname)
for line in fhandle:
    line = line.rstrip()
    if re.findall(reg_exp, line) != []:
        count += 1
print(fname + " had " + str(count) + " lines that matched " + reg_exp)
