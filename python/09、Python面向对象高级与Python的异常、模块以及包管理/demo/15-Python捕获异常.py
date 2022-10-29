try:
    f = open('python.txt', 'r')
    content = f.readline()
    print(content, end='')
except:
    f = open('python.txt', 'w', encoding='utf-8')
    f.write('发生异常，执行except语句中的代码')
f.close()