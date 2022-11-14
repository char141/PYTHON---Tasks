# code to find the number of times an email in a mailbox was received from each address 

dictionary_addresses = dict()
maximum = 0
minimum = 0
maximum_address = ""
minimum_address = ""
fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except FileNotFoundError:
    print("File not found!", fname)
    exit()
for line in fhandle:
    words = line.split()
    if len(words) < 2 or words[0] != "From":
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1
        else:
            dictionary_addresses[words[1]] += 1
print(dictionary_addresses)

for address in dictionary_addresses:
    if dictionary_addresses[address] > maximum:
        maximum = dictionary_addresses[address]
        maximum_address = address
    else:
        if dictionary_addresses[address] < minimum:
            minimum = dictionary_addresses[address]
            minimum_address = address
print("Frequent emails from: ", maximum_address, maximum)
print("Less emails from: ", minimum_address, minimum)
