# Write a function longest that accepts a List of Strings as an argument.

# It should return the longest String in the List.

def longest(e):
    return len(e)


list1 = ["Toyota", "Ford", "Chevrolet", "BMW", "Lexus", "Dodge", "Honda"]

list1.sort(key=longest)

print(list1[-1])