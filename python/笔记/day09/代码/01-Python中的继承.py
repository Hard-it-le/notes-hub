# 1、定义一共共性类（公共类）
class Person(object):
    # 定义__init__初始化方法
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # 定义相关方法
    def eat(self):
        print('i can eat food!')

    def speak(self):
        print('i can speak!')

# 2、定义个性类（Teacher）
class Teacher(Person):
    pass

# 3、定义个性类（Student）


teacher = Teacher('Smith', 35, 'New York')
teacher.eat()
teacher.speak()