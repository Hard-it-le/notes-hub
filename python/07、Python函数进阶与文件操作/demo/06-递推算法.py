# 递推算法：根据已知条件，求结果（或者根据结果求未知条件）
def recusive(n):
    """ 返回斐波那契数列某一位（n>=1）的结果 """
    if n == 1 or n == 2:
        return 1
    # 开始递推f(3) = f(2) + f(1)  f(4) = f(3) + f(2) ... f(15) = f(14) + f(13)
    dict1 = {1:1, 2:1}
    for i in range(3, n+1):
        # f(3) = f(2) + f(1)
        # f(i) = f(i-1) + f(i-2)
        dict1[i] = dict1[i-1] + dict1[i-2]
    return dict1[n]

# 函数调用
print(recusive(15))