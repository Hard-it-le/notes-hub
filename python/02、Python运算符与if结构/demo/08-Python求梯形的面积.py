a = float(input('请输入上底：'))
b = float(input('请输入下底：'))
h = float(input('请输入高：'))

# 求梯形的面积 = (上底 + 下底) * 高 / 2
s = (a + b) * h / 2
# 打印输出梯形的面积
print(f'梯形的面积：{s}')