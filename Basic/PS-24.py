# Problem Statement

'''Q.24 A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: The quick brown fox jumps over the lazy dog. Your task here is to write a
function to check a sentence to see if it is a pangram or not.'''

#-------Method 1 --------------
def pangram(sentance):
    sentance=set(list(sentance.lower()))
    count=0
    li = list('abcdefghijklmnopqrstuvwxyz')
    for i in li:
        if i in sentance:
            count+=1
    if count==26:
        return True

    return False

sentance = "The quick Brown Fox jumps over the Lazy Dog"
print('---------Using Method 1----------------')
print(sentance, 'is panagram : ',pangram(sentance))

#-------Method 2 --------------
import string
def is_pangram(sentance):
    alphabet = set(string.ascii_lowercase)
    return set(sentance.lower()) >= alphabet

sentance = "The quick Brown Fox jumps over the Lazy Dog "
print('\n---------Using Method 2----------------')
print(sentance, 'is panagram : ',is_pangram(sentance))





