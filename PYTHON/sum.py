count = 0
total = 0
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    try:
        numbers = float(number)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + numbers
print(total, count, total / count)
