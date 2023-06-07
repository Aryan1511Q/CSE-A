a=eval(input("Enter first sides of a triangle\n"))
b=eval(input("Enter second sides of a triangle\n"))
c=eval(input("Enter third side of a triangle\n"))
d=a+b+c
if d==180:
    print(f"The given sides {a},{b},{c} can form a Triangle")
else:
    print(f"The given sides {a},{b},{c} cann't form a Triangle")    
