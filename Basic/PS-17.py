# Problem Statemnt
''' Q17.  Write a function that takes a number and prints a list of its digits. Eg. if number is 250, then it should print:
2
5
0
'''
n = list(input("Enter a number:"))
print("----using for loop--------")
for i in n:
    print(i)
print("----using join() function--------")
print('\n'.join(n)) 