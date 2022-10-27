str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇e不打印')
        break
    print(i)
else:
    print('循环正常结束之后执行的代码')