rlst = []
def reverse(lst):
    '''
    objective: to reverse the elements of list without modifying the original list
    input parameters: lst -> list that is to be reversed
    return value: rlst, reverse of the given list
    '''
    
    #approach: using reverse() function recursively and appending the last element every time to the new list
    
    if lst == []:
        return rlst
    rlst.append(lst[-1])
    return reverse(lst[0:len(lst) - 1])
