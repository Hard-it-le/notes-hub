import time

try:
   f = open('python.txt', 'r')
   try:
       while True:
           content = f.readline()
           if len(content) == 0:
               break
           time.sleep(3)
           print(content, end='')
   except:
       # Ctrl + C（终端里面，其代表终止程序的继续执行）
       print('python.txt未全部读取完成，中断了...')
   finally:
       f.close()
except:
   print('python.txt文件未找到...')