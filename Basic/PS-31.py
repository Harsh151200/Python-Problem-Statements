# Problem Statement
"""
Q.31 Write a function that computes the list of the first 100 Fibonacci numbers.
"""

def fibonacci(n):
    a,b = 0,1
    lst, count = [],0
    if n < 1:
        return lst
    elif n == 1:
        lst.append(a)
        return lst
    else:
        while count < n:
            lst.append(a)
            temp = a + b
            a = b
            b = temp
            count += 1
    return lst

  
print(fibonacci(100))

