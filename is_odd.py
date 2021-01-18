
# Write an is_odd function that uses your is_even function to determine if a number is odd. 
# (That is, do not do the calculation - call a function that does the calculation.)

#Hint: You'll use the not keyword.

num = int(input("Please give me an even number:  "))
while True:
    if (num % 2) != 0:
        print("{0} is Odd".format(num)) 
    else:
        print("{0} is Even".format(num))
    break



