# 导入os模块
import os


# ① 在程序中，将当前目录切换到static文件夹
os.chdir('static')
# print(os.getcwd())

# ② 创建一个新images文件夹以及test文件夹
# os.mkdir('images')
# os.mkdir('test')

# ③ 获取目录下的所有文件
# print(os.listdir())
for file in os.listdir():
    print(file)

# ④ 移除test文件夹
os.rmdir('test')