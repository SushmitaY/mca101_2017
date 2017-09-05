def gcdRecurse( a , b ):
    '''
    objective: to calculate GCD of 2 numbers
    parameters: a -> first number
                b ->second number
    return value: gcd of two numbers
    '''
    #approach : using division algorithm recursively
    
    if b == 0:
        return a
    else:
        return gcdRecurse( b , a % b )

def main():
    '''
    objective: to calculate GCD of 2 numbers
    input values: x -> first number
                  y ->second number
    result: gcd of two numbers
    '''
    #approach : using function gcdRecurse
    x = int(input('Enter first number : '))
    y = int(input('Enter second number : '))
    print(' GCD of given numbers is : ' , gcdRecurse( x , y ))

if __name__ == '__main__':
    main()

print('End of program')
