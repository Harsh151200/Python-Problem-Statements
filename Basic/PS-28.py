# Problem Statement
""""Q.28 Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion. """
#Use Python Tutor to visualize execution process

def sum_list_using_for_loop(lst):
    sum = 0 
    for i in lst:
        sum += i
    return sum

def sum_list_using_while_loop(lst):
    sum = 0 
    i = 0
    while i<len(lst):
        sum += lst[i]
        i +=1
    return sum

def sum_list_using_recursion(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list_using_recursion(lst[1:])

lst = [11,22,33]
print("Using for Loop : ",sum_list_using_for_loop(lst))
print("Using while Loop : ",sum_list_using_while_loop(lst))
print("Using recursion : ",sum_list_using_recursion(lst))
