def increment(num):
    '''
    objective: to increment the value of a integer by 1
    input parameters: num -> number to be incremented by one
    return value: num + 1, successor of the given number
    '''
    '''
    approach: using '+' operator to add 1 to the input number
    '''
    return num + 1

def mySum(num1, num2):
    '''
    objective: to find the sum of two numbers
    parameters:  num1 -> first non negative integer
                 num2 -> second non negative integer
    return value: sum of num1 and num2
    '''
    '''
    approach: using function increment() and using mySum() recursively
    '''
    assert num1 >= 0 and num2 >= 0
    
    if num2 == 0:
        return num1
    else:
        return mySum(increment(num1), num2 - 1)


