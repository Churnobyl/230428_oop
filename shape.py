import math

class Shape:
    def __init__(self) -> None:
        pass
    
    def get_area(self):
        pass
    

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius
        
    def get_area(self):
        return round((self.radius ** 2) * math.pi, 2)


class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    

shape = Shape()
print(shape.get_area())

circle = Circle(20)
print(circle.get_area())

rectangle = Rectangle(20, 40)
print(rectangle.get_area())