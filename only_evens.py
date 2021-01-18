# Write a function that accepts a List of numbers as an argument.

# Return a new List that includes the only the even numbers.

# only_evens([11, 20, 42, 97, 23, 10])
# Returns [20, 42, 10]

# Hint: use your is_even() function to determine which numbers to include in your new List.

only_evens = [11, 20, 42, 97, 23, 10]

for num in only_evens:
    if num % 2 == 0:
        print(num,  end = " ")
        

