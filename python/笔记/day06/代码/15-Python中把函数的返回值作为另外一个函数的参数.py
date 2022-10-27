# 定义一个test1函数
def test1():
    # 忽略中间的运算过程
    return 50

# 定义一个test2函数
def test2(num):
    print(num)

# 定义一个变量接收test1函数的返回值
result = test1()
# 调用test2函数
test2(result)
