import time

# 返回：格林制时间到当前时间的秒数
start = time.time()

# 编写递归函数
def func(n):
    if n == 10:
        return 1
    return (func(n+1) + 1) * 2

print(func(1))

end = time.time()
print(f'以上代码共执行了{end - start}s')