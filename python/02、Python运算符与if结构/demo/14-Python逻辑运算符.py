a = 1
b = 2
c = 3

print((a > b) and (b > c))  # False
print((a > b) or (b > c))   # False
print((a < b) or (b > c))   # True
print(not (a > b))          # True