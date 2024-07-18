import math


class Shape:
    def area(self):
       raise NotImplementedError("derived classes need to override this method")
class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length=length
        self.width=width
    def area(self):
        return f"The area of the Rectangle is: {self.length*self.width}"
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
    def area(self):
        return f"The area of the Circle is: { math.pi * (self.radius**2)}"