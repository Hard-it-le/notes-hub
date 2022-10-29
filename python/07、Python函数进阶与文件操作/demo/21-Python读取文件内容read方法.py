# 1、打开文件
f = open('python.txt', 'r', encoding='utf-8')
# 2、使用read()方法读取文件所有内容
contents = f.read()
print(contents)
# 3、关闭文件
f.close()