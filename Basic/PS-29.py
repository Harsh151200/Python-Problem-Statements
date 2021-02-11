# Problem Statement
"""
Q.29 Write a function that combines two lists by alternatingly taking elements,
  e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3] (assuming both lists are of equal lengths)
"""
def combine_alter_list_ele(lst1, lst2):
    dummy_lst = list()
    for i in range(len(lst1)):
        dummy_lst.append(lst1[i])
        dummy_lst.append(lst2[i])
    return dummy_lst

lst1 = [11,22,33,44,55]
lst2 = ['a','b','c','d','e']
print(combine_alter_list_ele(lst1,lst2))
