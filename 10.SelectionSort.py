def findMinimumIndex(lst, lower,  i = 0, i_min = 0 ):
    '''
    objective: to find the index of minimum element of the given list

    parameters: lst -> the list in which the the index of the minimum element is to be found according to lower and upper bound
                lower -> stores the index of the lower bound
                i -> i is an iterative value that is used to traverse the list from lower bound to end of the list
                i_min -> stores the index of the minimum element of the sublist

    return value: the index of the minimum element of the sublist
                
    '''

    # Approach : comparing the element at index i against the element at index i_min. If lst[i] < lst[i_min] is encountered, i_min is updated with value of i.
    
    if (i + lower) == len(lst):
        return (i_min + lower)
    if lst[i + lower] < lst[i_min + lower] :
        i_min = i    
    i = i + 1
    return findMinimumIndex(lst, lower, i, i_min)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

def selectionSort( lst , i = 0):
    '''
    objective : to sort a given list

    parameters : lst -> unsorted list that is to be sorted
                 i -> parameter holding the lower bound index
    '''

    #approach : finding the minimum element out of the unsorted part of list and push it on sorted part of list
    
    if( i == len(lst)):
        return
    else:
         mins = findMinimumIndex( lst, i )
         temp = lst[mins]
         lst[mins] = lst[i]
         lst[i] = temp
         return selectionSort(lst, i + 1)


#----------------------------------------------------

test = [30,20,10,5,13,86]
print('\n\nUnsorted List : ', test)
selectionSort(test)
print('\n\nSorted List : ', test)

