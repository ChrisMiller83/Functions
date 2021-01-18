
def largest_num(e):
    return (e)

list1 = [200, 12, 33, 56, 7, 890, 0.1, -100]
list2 = [3, 22, 45, 2, 435, 67, 5, 89, -20]
final_list = list1 + list2

final_list.sort(key=largest_num)
print(final_list, end = " ") 
print(" Is the list of all numbers.")

print(final_list[-1], " Is the largest number in the list.")


