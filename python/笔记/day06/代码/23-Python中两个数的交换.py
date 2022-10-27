# c1 = 10
# c2 = 2
#
# # 引入临时变量temp
# temp = c2
# c2 = c1
# c1 = temp
#
# print(c1, c2)


# c1 = 10
# c2 = 2
#
# c1 = c1 + c2  # 12
# c2 = c1 - c2  # 期望值c2 = 10
# c1 = c1 - c2  #
#
# print(c1, c2)


c1 = 10
c2 = 2

c1, c2 = c2, c1
print(c1, c2)