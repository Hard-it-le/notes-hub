students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

# 按name值升序排列
# students.sort(key=lambda x:x['name'])
# print(students)

# 按name值升序排列
students.sort(key=lambda x:x['name'], reverse=True)
print(students)

# 按age值升序排列
# students.sort(key=lambda x:x['age'])
# print(students)