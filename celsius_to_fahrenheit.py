
def celsius_to_fahrenheit(Celsius):
    user_input = Celsius
    return ((user_input -32) * 5/9)

temp = int(input("Please enter a temperature you want to convert from celsius to fahrenheit.   "))
print(celsius_to_fahrenheit(temp), "degrees Fahrenheit")





