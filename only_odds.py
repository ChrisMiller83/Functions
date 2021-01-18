# Write a function that accepts a List of numbers as an argument.

#Return a new List that includes the only the odd numbers.

only_odds = [11, 20, 42, 97, 23, 10]

for num in only_odds:
    if num % 2 != 0:
        print(num,  end = " ")