def myCosine(n):
    '''
    objective: to calculate cosine of a number
    approach: using series
    input parameter: n -> the number whose cosine needs to be calculated
    result: cosine of a number
    '''
    term = 1
    total = 0;
    multiplyBy = - n ** 2
    divideBy = 1
    nextIntSeq = 1
    epsilon = 0.0001

    while abs(term) > epsilon:

        total += term
        divideBy = nextIntSeq * (nextIntSeq + 1)
        term *= multiplyBy / divideBy
        nextIntSeq += 2

    return total

def main():
    '''
    objective: to calculate cosine of a number
    result: cosine of a number
    '''
    #approach: using function myCosine
    
    n = float(input('Enter a number whose cosine: '))
    result = myCosine(n)
    print('\nCosine(', n ,') : ', result)

    print('End of main')

if __name__ == '__main__':
    main()

print('End of function')
              
