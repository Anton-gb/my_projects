class Auto:
    def __init__(self):
        self.age = 0



class Aut(Auto):
    def __init__(self, name):
        super().__init__()
        self.ag = 0
        self.name = name


a = Aut('r')
print(a.age)

