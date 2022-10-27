fn1 = lambda *args : args
fn2 = lambda **kwargs : kwargs

print(fn1(10, 20, 30))
print(fn2(name='Tom', age=20, address='北京市海淀区'))