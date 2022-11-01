def chop(newlist):
    del newlist[0]
    del newlist[-1]

while True:
    mylist = input("Enter a value: ")
    if mylist == "done":
        break
    lst = list(mylist)
    chopped_list = chop(lst)
    print(mylist)
    print(lst)
    print(chopped_list)
