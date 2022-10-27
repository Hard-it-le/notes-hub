# 定义一个Student类
class Student():
    # 定义魔术方法，用于初始化属性信息
    def __init__(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile
    # 定义魔术方法，用于打印输出学员信息
    def __str__(self):
        return f'学员姓名：{self.name}, 学员年龄：{self.age}, 学员电话：{self.mobile}'
