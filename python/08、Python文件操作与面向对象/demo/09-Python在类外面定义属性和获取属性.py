# 1、定义一个Person类
class Person():
    pass

# 2、实例化Person类，生成p1对象
p1 = Person()
# 3、为p1对象添加属性
p1.name = '老王'
p1.age = 18
p1.address = '北京市顺义区京顺路99号'

# 4、获取p1对象的属性
print(f'我的姓名：{p1.name}')
print(f'我的年龄：{p1.age}')
print(f'我的住址：{p1.address}')