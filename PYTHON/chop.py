def chop(newlist):
    del newlist[0]
    del newlist[-1]

def middle(newlist):
    lst1 = newlist[1:]
    del lst1[-1]
    return lst1

while True:
    mylist = input("Enter a list: ")
    if mylist == "done":
        break
    lst = list(mylist)
    chopped_list = chop(lst)
    print(mylist)
    print(lst)
    print(chopped_list)
    middle_list = middle(lst)
    print(middle_list)
