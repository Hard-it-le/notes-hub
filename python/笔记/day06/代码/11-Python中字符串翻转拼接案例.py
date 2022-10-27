def func(str1):
    # 方法一：对字符串进行翻转操作(切片)
    str1 = str1[::-1]
    return str1.replace('.', '-')
    # 方法二：使用split切割，然后reverse进行翻转
    # list1 = str1.split('.')
    # list1.reverse()
    # return '-'.join(list1)


# 调用函数实现字符串翻转拼接
str1 = '1.2.3.4.5'
print(func(str1))  # 5-4-3-2-1