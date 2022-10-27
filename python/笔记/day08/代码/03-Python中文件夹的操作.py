# 导入os模块
import os


# 1、使用mkdir方法创建一个images文件夹
# os.mkdir('images')
# os.mkdir('images/avatar')

# 2、getcwd = get current work directory
print(os.getcwd())

# 3、os.chdir，ch = change dir = directory切换目录
os.chdir('images/avatar')
print(os.getcwd())

# 切换到上一级目录 => images
os.chdir('../../')
print(os.getcwd())

# 4、使用os.listdir打印当前所在目录下的所有文件，返回列表
print(os.listdir())

# 5、删除空目录
os.rmdir('images/avatar')