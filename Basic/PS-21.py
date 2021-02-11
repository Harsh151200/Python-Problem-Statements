# Problem Statement
'''Q.21 Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.'''

#Defining a function to return list corresponding to length of each elements in a given list 
def len_each_list_elements(lst):
    len_list = list()
    for i in lst:
        len_list.append(len(i))
    return len_list

lst = ['Hii', 'how', 'are', 'you', '?']
print(lst)
print(len_each_list_elements(lst))

