# 1、add方法增加单一数据
# students = set()
# students.add('李哲')
# students.add('刘毅')
# students.add('李哲')
# print(students)

# 2、update方法增加序列类型数据
students = set()
list1 = ['刘备', '关羽', '赵云']
students.update(list1)
print(students)