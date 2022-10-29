# 1、定义一个类
class Person():
    # 定义一个方法
    def speak(self):
        print(self)
        print('Nice to meet you!')

# 2、类的实例化（生成对象）
p1 = Person()
print(p1)
p1.speak()