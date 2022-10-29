def print_lines(num, length):
    """ print_lines函数主要作用用于生成多条指定长度的横线，拥有两个参数num和length，都是int整型数据，num用于控制生成的横线数量，length用于控制生成横线的长度 """
    for i in range(num):
        print('-' * length)


# 调用函数
# help(print_lines)
print_lines(5, 60)