def areaTriangle( base , height ):
    
    '''
    objective : to calculate the area of a triangle
    approach  : multiplying base, height together and then taking half of it
    parameteres : -> base : base of triangle
                  -> height : height of triangle
    return value : area of the triangle 
    '''
    
    area =  0.5 * base * height
    
    return area

def main():
    
    '''
    objective : to calculate the area of a triangle
    approach  : taking base and height of triangle as input from user and passing them to function areaTriangle
    '''
    
    base = int( input('Enter base of triangle : ') )
    height = int( input('Enter height of triangle : ') )
    area = areaTriangle( base , height)
    
    print(' Base of triangle : ' , base)
    print(' Height of triangle : ' , height)
    print(' Area of triangle : ', area)
    
    print(' End of main ')
    
if __name__ == '__main__':
    main()
    
print(' End of program ')
