def findIndex(ele,lst,upper,indx = 0):
    '''
    objective: to find the index at which the element would be inserted
    input parameters: -> ele - element to be inserted
                      -> lst - sorted list in which element is to be inserted
                      -> indx - index
    return value: index of the position where the given element is to be inserted so that the list remain sorted
    '''

    #approach : function findIndex() is called recursively untill the first element of the list becomes greater than the element to be added
    
    if indx > upper :
        return indx
    if lst[0] < ele:
        return findIndex(ele, lst[1:], upper, indx+1)
    else:
        return indx
    
def insertElement(ele, lst, upper):
    '''
    objective: to insert a given element at correct position in a sorted list
    input parameters: -> ele - element to be added
                      -> lst - sorted list in which element is to be added
    
    '''
    #approach : correct index is evaluated using function findIndex(), then the given element is inserted at the resultant index

    indx = findIndex(ele,lst,upper)
    lst.insert(indx,ele)

def mySort( lst, i = 0 ):
    '''
    objective : to sort the given list
    input parameters : lst -> list to be sorted
    '''

    #approach: using recursion and function insertElement(...)

    if i == len(lst) - 1:
        return
    else:
        ele = lst[i+1]
        del lst[i+1]
        insertElement(ele, lst, i)
        return mySort( lst, i + 1)

#----------------------------------------------
    
x = [10,30,5,20,80,25,7,8]
print('\nUnsorted List : ', x)
mySort(x)
print('\nSorted List : ', x)
