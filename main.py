first_num = 39
second_num = 54
# Это функция сумматор
def add(a: int, b: int) -> int:
    return a + b

print(add(first_num, second_num))

class deploy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def coord(self):
        return self.x, self.y
    
d = deploy(20, 40)

print(d.coord)

