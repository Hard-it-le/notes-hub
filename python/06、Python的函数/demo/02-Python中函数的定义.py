# 1、封装一个函数greet，定义一个参数name
def greet(name):
    return name + '，您好'

# 2、见到同事老张
print(greet('老张'))

# 3、见到同事老李
print("\033[0;31;40m\t" + greet('老李') + "\033[0m")

# 4、见到同事老王
print("\033[0;36;40m\t" + greet('老王') + "\033[0m")