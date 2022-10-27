import random


# 第一步：提示输入输入石头剪刀布，0-代表石头，1代表剪刀，2代表布
player = int(input('请输入您的出拳0-代表石头，1代表剪刀，2代表布：'))
# 第二步：电脑随机出拳(后续解决)
computer = random.randint(0, 2)

print(computer)

# 第三步：根据用户以及计算机的出拳判断输赢
# 什么情况，玩家会赢
# player==0且computer==1 或 palyer==1且computer==2 或 player==2且computer==0
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player==2 and computer == 0):
	print('玩家获胜')
elif player == computer:
	print('平局')
else:
    print('电脑获胜')