import random
# 第一步：定义一个计数器
i = 0
# 第四步：生成1 ~ 10之间的随机数
secretNum = random.randint(1, 10)
# 第二步：编写循环条件
while i < 3:
    # 第五步：提示用户输入一个数字
    userNum = int(input('请输入您猜的数字（范围1~10之间）:'))
    # 第六步：判断用户输入的数字是否与随机数相等
    if secretNum == userNum:
        print('恭喜你，才对了')
        break
    elif secretNum < userNum:
        print('猜大了')
    elif secretNum > userNum:
        print('猜小了')
    # 第三步：更新计数器
    i += 1