# 1、定义一个字典
cat = {'name':'Tom', 'age':5, 'address':'美国纽约'}
# 2、获取字典的相关信息
name = cat.get('name')
age = cat.get('age')
gender = cat.get('gender', 'male')  # get(key, 默认值)
address = cat.get('address')
print(f'姓名：{name}，年龄：{age}，性别：{gender}，住址：{address}')