# str1 = ' '
# print(str1.isspace())

username = input('请输入的您的用户名：')
if len(username) == 0 or username.isspace():
    print('您没有输入任何字符...')
else:
    print(f'您的输入的字符{username}')