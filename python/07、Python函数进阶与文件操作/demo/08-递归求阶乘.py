def f(n):
    # 编写递归结束条件
    if n <= 2:
        return n
    # ...递归等式
    return f(n-1) * n

print(f(10))