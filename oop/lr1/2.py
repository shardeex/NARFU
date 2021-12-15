# Решить задачу определения високосный год или нет с применением класса.

class Year():
    def __init__(self, year: int):
        self.year = year
    
    def is_leap(self) -> str:
        return f'{self.year} {"is" if self.year % 400 == 0 or (self.year % 100 != 0 and self.year % 4 == 0) else "is not"} leap'

new_year = Year(1604)
print(new_year.is_leap())