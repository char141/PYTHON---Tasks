import re
rev = []
fname = 'mbox-short.txt'
fhandle = open(fname)
for line in fhandle:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    for val in x:
        val = float(val)
        rev = rev + [val]
x_sum = sum(rev)
print(x_sum)
count = float(len(rev))
print(count)
x_avg = x_sum / count
print(x_avg)

