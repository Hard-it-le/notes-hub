import random

# 1、定义3间教室以及8名讲师
rooms = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# 2、对所有的讲师进行遍历操作
for teacher in teachers:
    # 3、生成随机数
    index = random.randint(0, 2)
    rooms[index].append(teacher)
# 3、输出每个教室的讲师信息
# print(rooms)
i = 1
for room in rooms:
    print(f'第{i}个教室中的讲师：{room}')
    i += 1