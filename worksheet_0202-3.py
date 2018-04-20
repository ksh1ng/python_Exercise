import math
def  cylinder_V(r,h):
    return math.pi*r**2*h
radius=int(input("Type the radius for a cylinder:"))
height=int(input("Type the height for a cylinder:"))
print(cylinder_V(radius,height))
