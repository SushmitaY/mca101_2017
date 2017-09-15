#-------------------------*********** FINDING MINIMUM ELEMENT's INDEX IN A SUBLIST ***********----------------------------------


#-------------------------------------------------------------------------------------------------------------------------------

def findMinimumIndex(lst, i, upper, i_min ):
    '''
    objective: to find the index of minimum element of the given list

    parameters: lst -> the list in which the the index of the minimum element is to be found according to lower and upper bound
                upper -> stores the index of the upper bound 
                i -> i is an iterative value that is used to traverse the list from lower bound to upper bound
                i_min -> stores the index of the minimum element of the sublist

    return value: the index of the minimum element of the sublist
                
    '''

    # Approach : comparing the element at index i against the element at index i_min. If lst[i] < lst[i_min] is encountered, i_min is updated with value of i.
    
    if i == upper + 1:
        return i_min
    if lst[i] < lst[i_min] :
        i_min = i    
    i = i + 1
    return findMinimumIndex(lst, i, upper, i_min)

#-------------------------------------------------------------------------------------------------------------------------------

def findMinimum(lst, lower, upper):
    '''
    objective: to find the index of minimum element of the given list

    parameters: lst -> the list in which the the index of the minimum element is to be found according to lower and upper bound
                lower -> stores the index of the lower bound
                upper -> stores the index of the upper bound 

    return value: the index of the minimum element of the sublist
                
    '''
    # Approach : using function findMinimumIndex(...)

    return findMinimumIndex(lst, lower, upper, lower)

#--------------------------------TEST CASES---------------------------------------------------------------------------------------

lst1 = [10, 20, 5, 40, 27, 30, 45, 80, 43, 12, 9]

print(lst1)
print( "Minimum index of sublist  ",lst1[4:10]," is = ", findMinimum(lst1, 4, 9) )   
print( "Minimum index of sublist  ",lst1[0:11]," is = ", findMinimum(lst1, 0, 10) )
print( "Minimum index of sublist  ",lst1[3:8]," is = ", findMinimum(lst1, 3, 7) )
print( "Minimum index of sublist  ",lst1[2:10]," is = ", findMinimum(lst1, 2, 9) )
print( "Minimum index of sublist  ",lst1[7:9]," is = ", findMinimum(lst1, 7, 8) )

    
