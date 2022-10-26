count = 0
total = 0
filename = input("Enter a file name: ")
fhandle = open(filename)
for line in fhandle:
    line = line.rstrip()
    if line.find('X-DSPAM-Confidence: 0.8475') == -1:
        continue
    print(line)
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        number = line.find(':')
        num = line[number + 1:]
        floating = num.strip()
        floatingpoint = float(floating)
        total = total + floatingpoint
        avg = total / count
    print("The average spam confidence is : ", avg)

