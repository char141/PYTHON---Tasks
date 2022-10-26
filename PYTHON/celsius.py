Temp = input("Enter temperature in degrees celsius: ")
try:
    celsius = float(Temp)
    fahrenheit = (celsius * 1.8) + 32
    print(str(celsius) +" degree celcius is equal to " +str(fahrenheit) +" degrees fahrenheit")
except:
    print("Please put a valid entry")
