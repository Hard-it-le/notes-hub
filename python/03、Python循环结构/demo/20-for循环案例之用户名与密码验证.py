# 定义变量，用于记录登录次数
trycount = 0
# 循环3次，因为超过3次就会报错
for i in range(3):
    # 更新登录次数
    trycount += 1
    # 提示用户输入账号与密码
    username = input('请输入您的登录账号：')
    password = input('请输入您的登录密码：')

    # 判断用户名是否正确
    if username == 'admin':
        # 判断密码是否正确
        if password == 'admin888':
            print('恭喜你，登录成功')
            break
        else:
            print('密码错误')
            print(f'您还有{3 - trycount}次输入机会')
    else:
        print('用户名错误')
        print(f'您还有{3 - trycount}次输入机会')