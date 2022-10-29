def return_num():
    # 记住：在函数内部，当代码执行到return时，系统会自动认为函数到此执行结束
    return 1
    # 后续代码不会再次执行
    return 2


result = return_num()
print(result)