# 1、整型转浮点类型 int => float
num1 = 10
print(float(num1))
print(type(float(num1)))

print('-' * 20)

# 2、浮点类型转换为整型 float => int，浮点转整型，其小数点后的数据会丢失！！！
num2 = 18.88
print(int(num2))

print('-' * 20)

# 3、把字符串类型转换为整型或浮点类型
str1 = '20'
str2 = '10.88'
print(type(int(str1)))
print(type(float(str2)))