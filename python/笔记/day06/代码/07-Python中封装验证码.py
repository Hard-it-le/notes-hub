# 定义一个generate_code()函数
def generate_code(num):
    """ generate_code方法主要用于生成指定长度的验证码，有一个num参数，需要传递一个int类型的数值，其return返回结果为num长度的随机验证码 """
    import random
    # 第一步：定义一个字符串
    str1 = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
    # 第二步：循环num次，代表生成num长度的字符串
    code = ''
    for i in range(num):
        # 第三步：从字符串中随机抽取num个字符
        index = random.randint(0, len(str1) - 1)
        code += str1[index]
    # 第四步：使用return返回验证码
    return code

# 求帮助（查看generate_code函数的作用以及需要传递的参数）
# help(generate_code)

# 调用函数
print(generate_code(6))