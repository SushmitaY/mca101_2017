i = 0;
def increment(num):
    '''
    objective: to increment the value of a integer by 1
    input parameters: num -> number to be incremented by one
    return value: num + 1, successor of the given number
    '''
    '''
    approach: using '+' operator to add 1 to the input number
    '''
    return  num + 1

def pred(num):
    '''
    objective: to find predecessor of a given number
    input parameters: num -> number of which predecessor needs to be found
    return value: predecessor of the given number
    '''
    
    #approach: using function pred() reculsively
    
    global i
    if num == 0:
        return 0
    if increment(i) == num:
        return i
    else:
        i = increment(i)
        return pred(num)
    
