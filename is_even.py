# Write a function that accepts a number as an argument and returns a Boolean value. 
# Return True if the number is even; return False if it is not even.

num = int(input("Please give me an even number:  "))
while True:
    if (num % 2) == 0:
        print("{0} is Even".format(num)) 
    else:
        print("{0} is Odd".format(num))
    break