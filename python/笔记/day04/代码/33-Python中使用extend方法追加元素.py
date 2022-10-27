list1 = ['Tom', 'Rose', 'Jack']
# 1、使用extend方法追加元素"Jennify"
# names.extend("Jennify")
# print(names)

# 2、建议：使用extend方法两个列表进行合并
list2 = ['Hack', 'Jennify']
list1.extend(list2)

print(list1)