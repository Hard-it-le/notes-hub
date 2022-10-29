# 1、导入os模块
import os

# 2、定义一个要重命名的目录
path = 'static'

# 3、切换到上面指定的目录中
os.chdir(path)

# 5、定义一个标识，用于确认是添加字符还是删除字符
flag = int(input('请输入您要执行的操作（1-添加字符，2-删除字符）：'))

# 4、对目录中的所有文件进行遍历输出 => os.listdir()
for file in os.listdir():
    # 5、判断我们要执行的操作（1-添加字符，2-删除字符）
    if flag == 1:
        # 01.txt => python-01.txt
        newname = 'python-' + file
        # 重命名操作
        os.rename(file, newname)
        print('文件批量重命名成功')
    elif flag == 2:
        # python-01.txt => 01.txt
        index = len('python-')
        newname = file[index:]
        # 重命名操作
        os.rename(file, newname)
        print('文件批量重命名成功')
    else:
        print('输入标识不正确，请重新输入...')
