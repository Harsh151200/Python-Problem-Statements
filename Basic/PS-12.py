#Problem Statements
# Write a function that takes a list as input and returns the elements on odd positions in a list.

def list_return_odd_position():
    list_of_integers = list(input("Enter a multiple numbers with space between them : ").split())
    print("Your List is : ",list_of_integers)
    for i in range(len(list_of_integers)):
        if i%2 != 0:
            print(list_of_integers[i])

list_return_odd_position()