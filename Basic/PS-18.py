# Problem Statement
# Q.18 Replicate len()'s logic

def length(object):
    count = 0
    for i in object:
        count += 1
    return count

print("Length of list",length([11,22,33]))
print("Length of String",length('String'))
print("Length of dictionary",length({'list':1,'lsit2':'2'}))
# print(length(1242)) #length() won't work with int. It will give error