# 1、提示用户输入我们球队与其他三个球队的实力
a = int(input('请输入我们球队的实力值：'))
b = int(input('请输入1号球队的实力值：'))
c = int(input('请输入2号球队的实力值：'))
d = int(input('请输入3号球队的实力值：'))

# 2、开始比赛，求每次比赛的成绩
avsb = (a > b) * 3 + (a == b)
avsc = (a > c) * 3 + (a == c)
avsd = (a > d) * 3 + (a == d)

# 3、总成绩
score = avsb + avsc + avsd

# 4、输出总成绩
print(f'我们球队最终的总成绩：{score}')