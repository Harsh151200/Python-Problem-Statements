#Problem Statement
''' Q.25 Find charecter frequency i.e input a Sentance and find how many times a particular charecter is repeated in list'''

#---------Method 1-----------------
def find_frequency(sentance):
    sentance_unique_charecters = list(set(sentance))
    dummy_dict = dict()
    for i in sentance_unique_charecters:
        dummy_dict[i] = 0
        for j in list(sentance):
            if i == j:
                dummy_dict[i] += 1
    return dummy_dict

print("------------- Method 1 ---------------")
print(find_frequency('What is your name ?'))

#------------- Method 2 ---------------
def queue_listr_dict(queue_listr):
    setVar=list(set(queue_listr))
    dict={}
    setCount=[]

    i=0
    j=0
    while i!=len(setVar):
        count = 0
        for x in queue_listr:
            if x==setVar[i]:
                 count+=1
        setCount.append(count)
        i+=1
    for l in setCount:
        random=setVar[j]
        dict[random] = l
        j+=1
    return dict
print("------------- Method 2 ---------------")
print(queue_listr_dict('What is your name ?'))