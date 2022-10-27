# 定义一个变量n，用于获取学生数量
n = int(input('请输入学生的数量：'))
# 定义一个变量，用于统计有多少人报数了
count = 0
# 开始循环
for i in range(1, n+1):
    # 判断数字尾数为7
    if i % 10 == 7:
        continue
    # 判断数值是7的倍数
    if i % 7 == 0:
        continue
    # 如果不满足以上if条件，则对count进行+1操作
    count += 1
print(f'{n}个同学，共报数{count}人')