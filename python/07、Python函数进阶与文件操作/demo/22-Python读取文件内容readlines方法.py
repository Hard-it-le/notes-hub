# 1、打开文件
f = open('python.txt', 'r', encoding='utf-8')
# 2、读取文件
lines = f.readlines()
for line in lines:
    print(line, end='')
# 3、关闭文件
f.close()