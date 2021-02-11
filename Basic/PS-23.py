# Problem Statement
# Q.23 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

def filter_long_words(lst,n):
    dummuy_lst = list() #Creating an empty list to store elements with length greater than n
    for i in lst:
        if len(i) > n:
            dummuy_lst.append(i)
    return dummuy_lst

lst,n = ['Hii', 'are','you', 'doing','fine', '?'],3
print(filter_long_words(lst,n))

    

            