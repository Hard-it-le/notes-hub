class Girl():
    def __init__(self, name):
        self.name = name
        self.__age = 18

xiaomei = Girl('小美')
print(xiaomei.name)
print(xiaomei.__age)