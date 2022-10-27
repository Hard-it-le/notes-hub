# 1、定义一个集合
products = {'萝卜', '白菜', '水蜜桃', '奥利奥', '西红柿', '凤梨'}
# 2、使用remove方法删除白菜这个元素
products.remove('白菜')
print(products)
# 3、使用discard方法删除未知元素
products.discard('玉米')
print(products)
# 4、使用pop方法随机删除某个元素
del_product = products.pop()
print(del_product)