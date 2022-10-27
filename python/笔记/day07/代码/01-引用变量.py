# a = 10
# print(id(a))

a = 10
b = a

a = 100
print(b)  # 10 或 100

print(id(a))
print(id(b))