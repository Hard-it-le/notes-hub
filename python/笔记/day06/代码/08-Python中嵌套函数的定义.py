def funcB():
    print('这是funcB函数的函数体部分...')


def funcA():
    print('-' * 40)
    print('这是funcA函数的函数体部分...')
    # 假设我们在调用funcA函数时，需要使用到funcB的相关功能，则可以嵌套到funcA方法中
    funcB()
    print('-' * 40)


# 调用funcA函数
funcA()