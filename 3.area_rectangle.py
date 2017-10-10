def areaRectangle( length , breadth ):
    
    '''
    objective : to calculate the area of a rectangle
    approach  : multiplying length and breadth together 
    parameteres : -> length : length of rectangle
                  -> breadth : breadth of rectangle
    return value : area of the rectangle 
    '''
    
    area =  length * breadth
    
    return area

def main():
    
    '''
    objective : to calculate the area of a rectangle
    approach  : taking length and breadth of rectangle as input from user and passing them to function areaRectangle
    '''
    
    length = int( input('Enter length of Rectangle : ') )
    breadth = int( input('Enter breadth of Rectangle : ') )
    area = areaRectangle( length , breadth )
    
    print(' Length of Rectangle : ' , length)
    print(' Breadth of Rectangle : ' , breadth)
    print(' Area of Rectangle : ', area)
    
    print(' End of main ')
