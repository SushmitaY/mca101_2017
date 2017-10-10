def myDeepCopy(lst, new_lst = []):
    '''
    objective : to perform deep copy over a list
    input parameters: lst -> The list to be copied
                      new_lst -> A new list that is a copy of original list
    '''
    #Approach : calling myDeepCopy recursively untill the entire list is exhausted
    if lst == []:
         return new_lst
    else:
        if isinstance(lst[0],list):
            new_lst.append(myDeepCopy(lst[0], []))
        else:
            new_lst.append(lst[0])
        return myDeepCopy(lst[1:], new_lst)

#-----------------TEST CASE--------------------------------

a = [1,[2,[3,[4]]],8,9,14,[45,65,32]]
print(a)
b = myDeepCopy(a)
print(b)
