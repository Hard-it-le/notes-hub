# 1、查找某个元素在列表中出现的位置（索引下标）
list1 = ['apple', 'banana', 'pineapple']
print(list1.index('apple'))  # 0
# print(list1.index('peach'))  # 报错

# 2、count()方法：统计元素在列表中出现的次数
list2 = ['刘备', '关羽', '张飞', '关羽', '赵云']
# 统计一下关羽这个元素在列表中出现的次数
print(list2.count('关羽'))

# 3、in方法和not in方法（黑名单系统）
list3 = ['192.168.1.15', '10.1.1.100', '172.35.46.128']
if '10.1.1.100' in list3:
    print('黑名单IP，禁止访问')
else:
    print('正常IP，访问站点信息')
