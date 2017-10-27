def merge( lst1, lst2, merged = []):

    '''
    Objective: Merge two sorted array(Using slicing)
    Input parameter: lst1 -> first sorted list
                     lst2 -> second sorted list
                     merged -> partially/completely merged list
    return value: merged list
    '''

    if(len(lst1) == 0):
        merged += lst2
        return merged

    if(len(lst2) == 0):
        merged += lst1
        return merged
    
    if( lst1[0] < lst2[0] ):
        merged.append(lst1[0])
        return merge(lst1[1:], lst2, merged)
    else:
        merged.append(lst2[0])
        return merge(lst1, lst2[1:], merged)


#-------------------------

print(merge([2,4,6,8,13,15], [5,7,19,23,45]) ) 
