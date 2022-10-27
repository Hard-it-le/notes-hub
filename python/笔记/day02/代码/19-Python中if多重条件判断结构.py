# 定义一个变量，接收用户输入的年龄
age = int(input('请输入您的年龄：'))
if age < 18:
    print('你还是一个童工，回去好好学习')
elif 18 <= age <= 60:
    print('合法工龄，可以正常工作')
elif age > 60:
    print('您已经达到了退休年龄，回家好好休息')
else:
    print('信息输入有误，请重新输入')