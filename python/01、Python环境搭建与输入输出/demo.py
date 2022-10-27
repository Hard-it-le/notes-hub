print('Hello World')

help('keywords')

name = 'testDemo'

address = '127.0.0.1'

print('name:'+name+':','address:'+ address)

# 数值类型、布尔类型、字符串类型、列表类型、元组类型、集合类型、字典类型
# int、float、boolearn、list、str、tuple、set、dict

print(type(name))
print(isinstance(name,int))
numbers = 1

type(numbers)
print(isinstance(name,str))

name = 'Tom'
age = 18
print(type(age))

names = '大白菜'
price = 3.5
print(type(names))

flag = True
print(flag)
print(type(flag))

num = 10
print(isinstance(num, int))  # True
print(isinstance(num, bool))  # False

msg = '这家伙很懒，什么都没有留下...'
print(msg)
print(type(msg))

# 1、list列表类型
list1 = [10, 20, 30, 40]
print(list1)
print(type(list1))

# 2、tuple元组类型
tuple1 = (10, 20, 30, 40)
print(tuple1)
print(type(tuple1))

# 3、set集合类型：去重
set1 = {10, 20, 30}
print(set1)
print(type(set1))

# 4、dict字典类型：查询、搜索
dict1 = {'name':'itheima', 'age':18}
print(type(dict1))


title = '大白菜'
price = 3.5
# 格式化输出“今天蔬菜特价了，大白菜只要3.5元/斤。"
print("今天蔬菜特价了，%s只要%.2f元/斤。" % (title, price))

id = 1
name = 'itheima'
print("姓名%s，学号%06d" % (name, id))



name = '孙悟空11'
mobile = '1887856909011'
print("姓名：{}，联系方式：{}".format(name, mobile))

name = '孙悟空11'
mobile = '1887856909011'
print(f'姓名：{name}，联系方式：{mobile}')

print('*\t*\t*')
print('hello\nworld')

password = input('请输入您的银行卡密码：')
print(f'您输入的银行卡密码为：{password}')

name = input('请输入您的姓名：')
age = input('请输入您的年龄：')

print(type(name))  # <class 'str'>
print(type(age))