
user_input = int(input("Please enter a number from 1 to 15. "))

for num in range(1, user_input + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    
    elif num % 3 == 0:
        print("fizz")
    
    elif num % 5 == 0:
        print("buzz")

    else:
        print(num)

            
        