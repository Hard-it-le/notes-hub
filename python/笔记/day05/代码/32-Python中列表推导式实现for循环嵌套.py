# list1 = []
# # 外层循环
# for i in range(1, 3):
#     # 内层循环
#     for j in range(0, 3):
#         tuple1 = (i, j)
#         list1.append(tuple1)
# print(list1)

list1 = [(i, j) for i in range(1, 3) for j in range(0, 3)]
print(list1)