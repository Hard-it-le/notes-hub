try:
    f = open('python.txt', 'r')
except FileNotFoundError as e:
    print(e)
