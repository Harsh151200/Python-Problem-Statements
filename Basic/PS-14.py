# Problem Statement
# Q14. Write a function which takes a list as input, and returns the reverse of that list as output.


'''-------------using inbuild functions----------------------'''
print("\nUsing inbuild fuction method")
demo_list = list(input("Enter a multiple numbers with space between them : ").split())
print("List before reverse",demo_list)
print("Using in-build reverse() function")
demo_list.reverse() 
print("List after reverse : ",demo_list)

'''-------------without using inbuild functions----------------------'''
print("\nWith using inbuild fuction method")
demo_list = []
for i in range(int(input("Enter range for list: "))):
    demo_list.append(input("Enter {} element:".format(i)))
print("List before reverse : ",demo_list)  
print("Using slicing index method")
'''Note : So [: stop] will slice list from starting till stop index and [start : ] will slice list from start index till end,
 Negative value of steps shows right to left traversal instead of left to right traversal,
  that is why [: : -1] prints list in reverse order.'''
print("Reversed List : ",demo_list[::-1])


