class ShortInputError(Exception):
    # length代表输入密码长度，min_length代表ShortInputError最小长度
    def __init__(self, length, min_length):
        self.length = length
        self.min_length = min_length

    # 定义一个__str__方法，用于输出字符串信息
    def __str__(self):
        return f'您输入的密码长度为{self.length}，不能少于{self.min_length}个字符'

try:
    password = input('请输入您的密码，不少于6位：')
    if len(password) < 6:
        raise ShortInputError(len(password), 6)
except Exception as e:
    print(e)
else:
    print(f'密码输入完成，您的密码是：{password}')