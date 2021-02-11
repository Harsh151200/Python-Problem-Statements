# Problem Statement
'''Q19. Define a function overlapping() that takes two lists and returns True if they have at least
one member in common, False otherwise. (break)'''

def overlapping(a,b):
    for i in a:
        if i in b:
            return True
    return False

list1 = [111,22,33,44]
list2 = [1,43,212,111]
print(overlapping(list1,list2))