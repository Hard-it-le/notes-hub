i = 1
result = 0

while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1

print(f'1~100之间所有偶数的和：{result}')