
user_input = int(input("Please enter a number under 50 for how many time you want it to loop. "))

n1, n2 = 0, 1
count = 0

if user_input <= 0:
    print("Please enter a positive number.")
elif user_input == 1:
    for i in range(2, user_input):
        print(i, end=', ')
   
    print("Fibonacci sequence upto", range, ":")
    print(n1)

elif user_input >= 51:
    print("That is too high a number.")

else:
    print("Fibonacci sequence:")
    while count < user_input:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

