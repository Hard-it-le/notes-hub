# 方法一：直接print打印
# print("*  *  *  *  *")
# print("*  *  *  *  *")
# print("*  *  *  *  *")
# print("*  *  *  *  *")
# print("*  *  *  *  *")

# 方法二：使用单层while循环
# i = 1
# while i <= 5:
#     print("*  *  *  *  *")
#     i += 1

# 方法三：使用单层while循环 + 运算符
# i = 1
# while i <= 5:
#     print("*  " * 5)
#     i += 1

# 方法四：使用while循环嵌套
i = 1
while i <= 5:
    # print("*  *  *  *  *")
    j = 1
    while j <= 5:
        print("*  ", end='')
        j += 1
    # 换行
    print('')
    i += 1