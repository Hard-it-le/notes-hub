def input_password():
    password = input('请输入您的密码，不少于6位：')
    if len(password) < 6:
        # 抛出异常
        raise Exception('您的密码长度少于6位')
        return
    # 如果密码长度正常，则直接显示密码
    print(password)


input_password()