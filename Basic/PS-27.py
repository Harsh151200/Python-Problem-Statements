#Problem Statements
"""Q.27 aaaaabaaaa = aba (remove redundant elements in a sequence) """

def remove_dedundant_elements(str):
    dummy_char = ''
    dummy_list = list()
    for i in str:
        if i != dummy_char:
            dummy_list.append(i)
        dummy_char = i
    return ''.join(dummy_list)
    
print(remove_dedundant_elements('aaaaabaaaa'))
print(remove_dedundant_elements('aabaacacccaddaffaaa'))

        