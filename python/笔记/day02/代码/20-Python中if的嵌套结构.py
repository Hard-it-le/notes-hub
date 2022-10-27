"""
根据条件（是否有钱）判断是否可以上车
money = 0 没钱
money = 1 有钱
"""
money = 1
seat = 0
if money == 1:
    # 有钱，可以上车
    print('有钱，可以上车')
    # if嵌套（seat = 1代表有空座，seat = 0代表没有空座）
    if seat == 1:
        # 有座位，可以坐下
        print('有座位，可以坐下')
    else:
        # 没有座位，只能站着回家了
        print('没有座位，只能站着回家了')
else:
    # 没钱，只能走路回家了
    print('没钱，只能走路回家了')
