from student import Student

content = "[{'name': 'Tom', 'age': 23, 'mobile': '10086'}, {'name': 'Jennifer', 'age': 18, 'mobile': '10000'}]"
# 把其转换为列表
data = eval(content)
# 遍历列表，把里面的字典转换为对象
# new_list = []
# for i in data:
#     new_list.append(Student(i['name'], i['age'], i['mobile']))
# print(new_list)

new_list = [Student(i['name'], i['age'], i['mobile']) for i in data]
print(new_list)