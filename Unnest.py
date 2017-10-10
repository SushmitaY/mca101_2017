def unnest(lst, newList = []):
    '''
    objective: To unnest a given nested list.
                e.g [1,[2,3],[4,[5,6],7]] -> [1,2,3,4,5,6,7]
    input parameter: lst -> Nested list.
                     newList -> Unnested List.
    return value: The unnested form of given input list.
    '''
    #Approach: Checks the first element of the list,
    #          if it is a list then calls the function unnest() over that list,
    #          otherwise appends that element in the newList
    #          then finally calls function unnest() for the list[1:]
    
    if len(lst) == 0:
        return newList
    elif isinstance(lst[0], list):
        unnest(lst[0], newList)
    else:
        newList.append(lst[0])
    return unnest(lst[1:], newList)
    
a = unnest([1,2,3,[4,[5,[6]]], 7, 8, 9])
