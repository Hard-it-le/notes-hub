# 定义一个变量，用于接收1~100的和
result = 0
# 从1开始循环，循环100次
for i in range(1, 101):
    result += i
print(f'1~100的和为{result}')