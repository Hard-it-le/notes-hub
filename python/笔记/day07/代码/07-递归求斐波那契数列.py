# 斐波那契数列 1 1 2 3 5 8 13 21 ...
def f(n):
    # 编写递归代码求第n位的结果
    if n == 1 or n == 2:
        return 1
    # 找出与斐波那契数列等价的关系式
    return f(n-1) + f(n-2)

# 调用函数
print(f(15))  # 610