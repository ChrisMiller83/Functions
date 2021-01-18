# Write a function shortest that accepts a List of Strings as an argument.

# It should return the shortest String in the List.

def shortest(e):
    return len(e)


list1 = ["Toyota", "Ford", "Chevrolet", "BMW", "Lexus", "Dodge", "Honda"]

list1.sort(key=shortest)

print(list1[0])


