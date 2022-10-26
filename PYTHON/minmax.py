largest = None
smallest = None
total = 0
count = 0
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    try:
        nums = int(number)
    except:
        print('Invalid input')
        continue
    if largest is None or nums > largest:
            largest = nums
    if smallest is None or nums < smallest:
            smallest = nums
    count = count + 1
    total = total + nums
print(count, total, largest, smallest)
