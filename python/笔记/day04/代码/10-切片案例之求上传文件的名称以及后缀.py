filename = 'avatar.png'
# 获取点号的索引下标
index = 6
# 使用切片截取文件的文件
name = filename[:index]
print(f'上传文件的名称：{name}')

# 使用切片截取文件的后缀
postfix = filename[index:]
print(f'上传文件的后缀：{postfix}')
