# 1、定义两个变量
c1 = '可乐'
c2 = '牛奶'

# 2、使用python将c1和c2的值进行交换（引入第三方变量，如temp）
# 第一步：首先把c2杯中的牛奶放入临时temp杯子中
temp = c2
# 第二步：把c1中值赋值给c2这个变量（相当于把c1中的可乐倒入c2中）
c2 = c1
# 第三步：把temp杯子中的牛奶倒入c1种
c1 = temp

print(f'1号杯中：{c1}')
print(f'2号杯中：{c2}')



str1 = "test1"

str2 = "test2"

print("两个数交换之前的值str1 =  %s，str2 = %s" % (str1, str2))

temps = str2

str2 = str1

str1 = temps


print("两个数交换之后的值str1 =  %s，str2 = %s" % (str1, str2))
