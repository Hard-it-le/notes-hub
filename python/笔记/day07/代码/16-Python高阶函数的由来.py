def fn(num1, num2, f):
    # f代表要传入的参数（参数是一个函数名，如abs或round）
    return f(num1) + f(num2)

# 绝对值求和
print(fn(-10, 10, abs))
# 四舍五入
print(fn(10.2, 6.9, round))