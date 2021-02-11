# Problem Statement
"""
Write a function that takes a list of strings an prints them, one per line, in a rectangular frame.
For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:

    *********
    * Hello *
    * World *
    * in    *
    * a     *
    * frame *
    *********
"""
def print_list_rectuangular_frame(lst):
    for i in range(len(max(lst,key=len))): #to print above * lines
        print('*',end = '')
    print('****')
    
    
    for j in lst:   #to take each string from list
            print('*',j,end='') #prints starting * with a whitespace and string
            white_space = len(max(lst,key=len)) + 1 - len(j)
            #calculation for white space after string is printed
            """whitespace = (length of maximum string in list) + (mandatory 1 whitespace after string) 
                                                  - (length of current string) 
            """
            for k in range(white_space):
                print(' ',end='')
            print('*\n')
    for i in range(len(max(lst,key=len))):
        print('*',end = '')
    print('****')

print_list_rectuangular_frame(["Hello","World", "in", "a", "frame"])

