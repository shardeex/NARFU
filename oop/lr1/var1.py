class Person:
    def __init__(self, weight: int, height: int):
        self.weight = weight
        self.height = height
    
    def calc_bmi(self) -> int:
        return self.weight / (self.height**2)

me = Person(56, 1.72)
friend = Person(44, 1.61)

print(me.calc_bmi())
print(friend.calc_bmi())