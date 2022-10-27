# dict1 = {i:i**2 for i in range(1,6)}
# print(dict1)

# list1 = ['name', 'age', 'gender']
# list2 = ['Tom', 20, 'male']
# # 结果：person = {'name':'Tom', 'age':20, 'gender':'male'}
#
# person = {list1[i]:list2[i] for i in range(len(list1))}
# print(person)

counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'ACER': 99}

# 需求：提取上述电脑数量大于等于200的字典数据
counts = {key:value for key, value in counts.items() if value >= 200}
print(counts)