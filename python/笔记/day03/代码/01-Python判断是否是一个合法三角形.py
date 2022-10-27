# 1、提示用户输入三角形的三边长度
a = int(input('请输入第一条边的长度：'))
b = int(input('请输入第二条边的长度：'))
c = int(input('请输入第三条边的长度：'))
# 2、判断两边之和是否大于第3条边
if (a + b > c) and (a + c > b) and (b + c > a):
    print('是一个合法的三角形')
else:
    print('不是一个合法的三角形')