# Problem Statement
# Q16. Write a function which takes as input two lists and returns a new list with elements of both those two lists.

list_1 = list(input("Enter values for List 1 with space between each element : ").split())
list_2 = list(input("Enter values for List 2 with space between each element : ").split())
list_3 = list_1 + list_2
print(list_1, '+', list_2, '=',list_3)
