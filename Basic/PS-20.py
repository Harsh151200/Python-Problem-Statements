# Problem Statement
''' Q20. Define a procedure histogram() that takes a list of integers and prints a histogram to the
screen. For example,histogram([4, 9, 7]) should print the following:

****
*********
*******
'''

def histogram(a):
    for i in a:
        print('\n')
        for j in range(i):
            print('*', end = " ")
    print('\n')
    return


histogram([4,9,7])
