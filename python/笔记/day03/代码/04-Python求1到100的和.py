# 第一步：初始化计数器
i = 1
# 第四步：定义一个result变量，用于接收累加后的结果
result = 0
# 第二步：编写循环条件
while i <= 100:
    # 第五步：循环累加变量i
    result += i
    # 第三步：更新计数器的值
    i += 1
print(f'1~100累加后的结果：{result}')