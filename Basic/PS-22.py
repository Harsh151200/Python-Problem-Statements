# Problem Statement
# Write a function find_longest_word() that takes a list of words and returns the length ofthe longest one.

#using max function
# max() ----> https://www.programiz.com/python-programming/methods/built-in/max
lst = ['Hii', 'hoaaswww', 'are', 'you', '?']
print('Using Max function\nLongest string in list is : ',max(lst,key=len))

#defining a user-defined function to the logic.
def find_longest_word(lst):
    longest_string_length = -1
    for i in range(len(lst)):
        if len(lst[i]) > longest_string_length:
            longest_string_length = len(lst[i])
            longest_string = lst[i]
    return longest_string

print("\nUsing user-defined function\nLongest string in list is : ",find_longest_word(lst))

