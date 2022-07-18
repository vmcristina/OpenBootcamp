def bisiesto ():
    year = int (input ("Introduce un año: "))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print ("El año que has indicado es bisiesto")
    
        
    else:
        print ("Este año NO es bisiesto")
        
    
        
    
bisiesto()
    