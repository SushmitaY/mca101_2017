def merge( lst1, lst2, i = 0, j = 0, merged = []):

    '''
    Objective: Merge two sorted array(Using index)
    Input parameter: lst1 -> first sorted list
                     lst2 -> second sorted list
                     i -> first index of unmerged part of list1
                     j -> first index of unmerged part of list2
                     merged -> partially/completely merged list
    return value: merged list
    '''

    if(len(lst1) == i) and (len(lst2) == j):
        return merged
    
    elif(len(lst1) == i):
        merged.append(lst2[j])
        j += 1
       
    elif(len(lst2) == j):
        merged.append(lst1[i])
        i += 1
    
    elif( lst1[i] < lst2[j] ):
        merged.append(lst1[i])
        i += 1
       
    else:
        merged.append(lst2[j])
        j += 1
        
    return merge(lst1, lst2, i, j, merged)


#-------------------------

print(merge([2,4,6,8,13,15], [5,7,19,23,45]) ) 
