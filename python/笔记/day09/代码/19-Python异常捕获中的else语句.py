try:
    f = open('python.txt', 'r')
except Exception as e:
    print(e)
else:
    content = f.readlines()
    print(content, end='')
    f.close()