def isoTriangle(s):
    
    '''
    objective: to draw isosceles triangle
    approach: printing multiple lines of symbols that this function has received as an argument
    parameter: -> s : the sysmbol that is to be used in triangle 
    '''
    
    print ('     ',s)
    print ('   ',s,s,s)
    print (' ',s,s,s,s,s)
    print ( s,s,s,s,s,s,s)

def main():
    
    '''
    objective: to take symbol input from user and draw isosceles triangle using that symbol
    approach: using function isoTriangle and passing the given symbol as parameter
    '''
    
    symbol = input("Enter a symbol you want to print : ")
    isoTriangle(symbol)
    
    print ('end of main')

if __name__ == '__main__':
    main()
print('end of program')
