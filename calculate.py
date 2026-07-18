
def Sum(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y



#Menu
print("""
**Menu**      

1-Sum
2-Subtraction
3-Multiply
4-Divide      
      """)

#choose menu    
try:
    Choose=int(input("Choose: "))
    
    x=int(input("Enter first num: "))
    y=int(input("Enter second num: "))
        

  
#functions  


    if Choose == 1:
        sum1=Sum(x,y)
        print(f"Its Equal >> {sum1}")
    elif Choose == 2:
        subtract1=subtract(x,y)
        print(f"Its Equal >> {subtract1}")
    elif Choose ==3:
        multiply1=multiply(x,y)
        print(f"Its Equal >> {multiply1}")
    elif Choose ==4:
        
        if y==0:
            print("Cannot divide by zero")
        else:
            divide1=divide(x,y)
            print(f"Its Equal >> {divide1}")
        
    else:print("Invaild Choice!")
    
except ValueError:
    print("Please use numbers")
    
    


    



    
        
 

     
        
        
        
        
        
