def putMaximumAt(lst, index, i = 0):
    '''
    objective: To insert the maximum uptill a given index to that index
    input parameters:lst -> The input list
                     index -> The position at which the maximum is to be inserted
    
    '''
    #Approach: To swap the ajdacent element, if the first element  is greater then second,
    #            till the index is reached.
    if i < index :
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
        return putMaximumAt(lst, index, i+1)
        
lst = [90,45,67,34,78,102,304,56,23,97]

putMaximumAt(lst, 4)
