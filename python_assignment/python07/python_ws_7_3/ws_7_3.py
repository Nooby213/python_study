# 아래 클래스를 수정하시오.
class Shape:
    
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return (self.width + self.length) * 2

shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)
