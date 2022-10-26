def count(string, letter):
    index = 0
    for character in string:
        if character == letter:
            index = index + 1
    print(index)
try:
    string = input("Enter string to check: ")
    letter = input("Enter letter to check: ")
    count(string, letter)
except:
    print("Error!")
