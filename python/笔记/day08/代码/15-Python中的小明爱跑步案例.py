# 1、定义Person类
class Person():
    # 2、初始化对象属性，name和weight
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    # 3、定义一个__str__方法打印对象的信息
    def __str__(self):
        return f'姓名：{self.name}，目前体重：{self.weight}KG'

    # 4、定义一个run方法代表跑步
    def run(self):
        self.weight -= 0.5

    # 5、定义一个eat方法代表吃饭
    def eat(self):
        self.weight += 1

# 6、实例化对象
xiaoming = Person('小明', 75.0)
print(xiaoming)

# 7、吃饭
xiaoming.eat()
print(xiaoming)

# 8、减肥跑步
xiaoming.run()
print(xiaoming)