# 1、定义一个Person类
class Person():
    def speak(self):
        print(f'我的名字：{self.name}，我的年龄：{self.age}，我的住址：{self.address}')

# 2、实例化Person类，生成p1对象
p1 = Person()
# 3、添加属性
p1.name = '孙悟空'
p1.age = 500
p1.address = '花果山水帘洞'
# 4、调用speak方法
p1.speak()