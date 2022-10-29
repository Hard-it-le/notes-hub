try:
    print(name)
    # print(10/0)
except (NameError, ZeroDivisionError) as e:
    print(e)