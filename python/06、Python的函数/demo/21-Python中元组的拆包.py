def func():
    # 经过一系列操作返回一个元组
    return 100, 200	 # tuple元组类型的数据

# 定义两个变量接收元组中的每个数组（拆包）
num1, num2 = func()
# 打印num1和num2
print(num1)
print(num2)