# Chat GPT exercises about Classes.

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(5, 3)
print(f'Length: {rectangle.length}.\nWidth: {rectangle.width}.')
print(f'The area is: {rectangle.area()}.')
print(f'The perimeter is: {rectangle.perimeter()}.')