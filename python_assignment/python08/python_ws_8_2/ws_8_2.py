# 아래 클래스를 수정하시오.
class Animal:
    def __init__(self):
        pass

    def bark(slef):
        return '동물은 운다.'
    
class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(slef):
        print('멍멍 !')

dog1 = Dog()
dog1.bark()
