def addElement(ele,lst):
    '''
    objective: to add a given element at correct position in a sorted list
    input parameters: -> ele - element to be added
                      -> lst - sorted list in which element is to be added
    return value: complete list with the new element added at correct position
    '''
    #approach : calls the addElement() function reculsively untill it finds that the first element of list is greater than the element to be added
    #           if the list gets empty, return the element itself
    #           if the first member is greater
    
    if len(lst) == 0:
        lst.append(ele)
        return lst
    if lst[0] < ele:
        f = lst[0]
        lst = addElement(ele, lst[1:])
        lst.insert(0, f)
        return lst 
    else:
        lst.insert(0,ele)
        return  lst

    
