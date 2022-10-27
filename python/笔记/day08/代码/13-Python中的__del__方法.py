class Person():
    # 构造函数__init__
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 析构方法__del__
    def __del__(self):
        print(f'{self}对象已经被删除')


# 实例化对象
p1 = Person('白骨精', 100)
# 删除对象p1
del p1