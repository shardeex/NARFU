# Создать класс объект кошки Cat, который будет принимать два аргумента, три
# метода по примеру выше и создать 2-3 экземпляра класса.

class Cat():
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = str
    
    def get_name(self) -> str:
        return f"Cat's name is {self.name}."
    
    def get_age(self) -> str:
        return f"Cat is {self.age} year(s) old."
    
    def sit(self) -> str:
        return f"{self.name} is now sitting."

black_cat = Cat('johnny', 2)
white_cat = Cat('billy', 5)
brown_cat = Cat('jessie', 3)
