# 定义一个全局变量
num = 10
# 定义一个功能，用于求两个数的和
def sum_num(num1, num2):
    return num1 + num2
# 定义一个类
class Person():
    pass

if __name__ == '__main__':
    # 模块测试代码
    print('-' * 40)
    print(num)
    print(sum_num(10, 20))
    p1 = Person()
    print(p1)
    print('-' * 40)