class Fruit(object):
    # 公共方法
    def makejuice(self):
        print('i can make juice')

class Apple(Fruit):
    def makejuice(self):
        print('i can make apple juice')

class Banana(Fruit):
    def makejuice(self):
        print('i can make banana juice')

class Orange(Fruit):
    def makejuice(self):
        print('i can make orange juice')

class Peach(Fruit):
    def makejuice(self):
        print('i can make peach juice')


# 定义公共方法如service
def service(obj):
    obj.makejuice()


apple = Apple()
banana = Banana()
orange = Orange()

for i in (apple, banana, orange):
    service(i)