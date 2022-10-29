# 定义一个函数
def func(names):
    # 在函数内部更改可变变量names
    names.append('赵六')
    print(names)


# 定义一个全局变量
list1 = ['张三', '李四', '王五']
# 调用函数
func(list1)
# 在全局作用域中打印list1
print(list1)