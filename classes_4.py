# Chat GPT exercises about Classes.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        if self.width != self.height:
            result = self.width * self.height
            return f'The area of the rectangle is: {result}.'
        else:
            result_sqr = self.width ** 2
            return f'The area of a square is: {result_sqr}.' 
    
    def perimeter(self):
        if self.width != self.height:
            result = 2 * (self.width + self.height)
            return f'The perimeter of the rectangle is: {result}.'
        else:
            result_sqr = self.width * 4
            return f'The perimeter of the square is: {result_sqr}.'
    
    def diagonal(self):
        diag = (self.width**2 + self.height**2) // 2
        
        if self.width != self.height:
            return f'The diagonal of a rectangle is: {diag}.'
        else:
            return f'The diagonal of a square is: {diag}.'
    
    def is_square(self):
        if self.width == self.height:
            return 'This is in fact a square!'
        else:
            return 'This is a rectangle.'
    

rect = Rectangle(2, 2)
print(f'{rect.area()}\n{rect.perimeter()}\n{rect.is_square()}\
      \n{rect.diagonal()}')