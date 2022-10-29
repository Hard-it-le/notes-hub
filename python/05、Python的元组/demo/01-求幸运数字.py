# 第一步：定义二个空列表
nums = []
lucky = []
# 第二步：提示用户输入数字
num = int(input('请输入您要输入的数字：'))
# 第三步：生成nums列表（把1到num）所有的数据都追加到nums列表中
for i in range(1, num+1):
    nums.append(i)
# 第四步：对nums进行遍历操作，获取幸运数字
for i in nums:
    if i % 6 == 0:
        # 幸运数字从nums中删除
        nums.remove(i)
        # 把幸运数字写入到lucky列表中
        lucky.append(i)
# 第五步：打印nums和lucky
print(nums)
print(lucky)