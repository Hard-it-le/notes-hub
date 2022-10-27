def average_num(num1, num2, num3):
    """ average_num函数主要用于生成3个数的平均值，一共有3个参数，num1、num2、num3，要求是整型或浮点类型的数据，其返回结果就是三个数的平均值 """
    sum = num1 + num2 + num3
    # 求平均值
    return sum/3

# 调用average_num方法
# help(average_num)
print(average_num(10, 20, 30))