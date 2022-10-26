def computepay(hours: float , rate: float):
    if hours > 40:
        rate = rate * 1.5
    pay = hours * rate
    return pay

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    netpay = computepay(hours, rate)
    print("Pay: ", netpay)
except:
    print("Enter valid values!")
