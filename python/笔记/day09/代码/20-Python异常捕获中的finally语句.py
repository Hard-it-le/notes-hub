try:
    f = open('python.txt', 'r')
except:
    f = open('python.txt', 'w')
else:
    print('哈哈，真开森，没有遇到任何异常')
finally:
    print('关闭文件')
    f.close()