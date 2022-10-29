str1 = 'hello world and hello linux and hello python'
# 不限定字符串长度
ands = str1.count('and')
# 限定开始查找的位置和结束位置
# ands = str1.count('and', 10, 30)
print(f'and字符串出现的次数为：{ands}')