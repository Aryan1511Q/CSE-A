print("To calculate the surface volume of cylinder and area of cylindr enter its radius and height\n")
radius=eval(input())
height=eval(input())
PI=3.14
volume=PI*radius*radius*height
SurfaceAreaOfCylinder=((2*PI*radius)*height)+((PI*radius*2)*2)
print("Surface volume of cylinder is", volume," Area of cylinder is ", SurfaceAreaOfCylinder)
