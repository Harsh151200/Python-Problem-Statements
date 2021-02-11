#Problem Statement
#Q10.Sum of all individual digits from a list of integer

list_of_integers = list(input("Enter a multiple numbers with space between them : ").split())
list_sum = 0
for x in list_of_integers:

    # for lst in list(x):
    #     list_sum += int(lst)

    list_sum += sum(map(int,x))
print(list_sum)

