#Sorts a list from the longest to the shorest word
txt = 'but soft what light in younder window breaks'
words = txt.split()
t = list()
for word in words: # builds a list of tuples, where each tuple is a word 
                            # preceded by its length.
    t.append((len(word), word))
t.sort(reverse = True) #keyword argument reverse=True tells sort to go in
                                #decreasing order.
res = list()
for length, word in t: # verses the list of tuples and builds a list of words 
                                # in descending
    res.append(word)
print(res)
