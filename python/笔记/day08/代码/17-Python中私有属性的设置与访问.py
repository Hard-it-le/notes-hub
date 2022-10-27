class Girl():
    def __init__(self, name):
        self.name = name
        self.__age = 18

    # 公共方法：提供给外部的访问接口
    def get_age(self):
        # 本人访问：允许直接访问
        # 外人访问：加上限制条件
        return self.__age

    # 公共方法：提供给外部的设置接口
    def set_age(self, age):
        self.__age = age


girl = Girl('小美')
girl.set_age(19)
print(girl.get_age())