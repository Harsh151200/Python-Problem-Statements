# Problem Statement
"""
Q.35 Write a function which will take two integers as input, and returns the Greatest Common Divisor (GCD) of those two numbers.
 (use the Euclid’s algorithm for the same)

 Link for Eucidian Algorithm example:
 https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.onlinemathlearning.com%2Feuclidean-algorithm.html&psig=AOvVaw2O-EZ0oUd-GxmcxXLEu7UP&ust=1601986363091000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKCE5LS2newCFQAAAAAdAAAAABAD
"""

def euclidian_gcd(a,b):
    while(b): #until b becomes 0 i.e until divisor becomes 0
        a,b = b,a%b
    return a

print(euclidian_gcd(5,15))
