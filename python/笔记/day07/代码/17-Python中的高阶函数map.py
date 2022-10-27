def func(n):
    return n ** 2

list1 = [1, 2, 3]

list2 = list(map(func, list1))
print(list2)