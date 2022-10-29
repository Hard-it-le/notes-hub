import functools


# 定义一个函数（求和）
def func(a, b):
    return a + b
# 定义一个列表
list1 = [10, 20, 30, 40, 50]
# 调用reduce高阶函数求列表中所有元素的和
sums = functools.reduce(func, list1)
print(sums)