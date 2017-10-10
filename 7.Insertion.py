def findIndex(ele,lst,indx):
    '''
    objective: to find the index at which the element would be inserted 
    input parameters: -> ele - element to be inserted
                      -> lst - sorted list in which element is to be inserted
                      -> indx - index 
    return value: index of the position where the given element is to be inserted so that the list remain sorted
    '''

    #approach : function findIndex() is called recursively untill the first element of the list becomes greater than the element to be added 
    
    if len(lst) == 0:
        return indx
    if lst[0] < ele:
        return findIndex(ele, lst[1:], indx+1)
    else:
        return indx
    
def insertElement(ele, lst):
    '''
    objective: to insert a given element at correct position in a sorted list
    input parameters: -> ele - element to be added
                      -> lst - sorted list in which element is to be added
    
    '''
    #approach : correct index is evaluated using function findIndex(), then the given element is inserted at the resultant index

    indx = findIndex(ele,lst,0)
    lst.insert(indx,ele)

#TEST CASES

test1 = [10,20,30,40]
insertElement(25, test1)
print("Result : ", test1)

test2 = [10,20,30,40]
insertElement(50, test2)
print("Result : ", test2)

test3 = [10,20,30,40]
insertElement(5, test3)
print("Result : ",test3)
