str = 'X-DSPAM-Confidence:0.8475'
pos1 = str.find(':')
print(pos1)
Last =str[pos1 + 1:]
last = float(Last)
print(last)
