def fahrenheit_to_Celsius(f):
    user_input = f
    return ((user_input * 9/5) + 32)

temp = int(input("Please enter a temperature you want to convert from fahrenheit to celsius.   "))

print(fahrenheit_to_Celsius(temp), "degrees Celsius")