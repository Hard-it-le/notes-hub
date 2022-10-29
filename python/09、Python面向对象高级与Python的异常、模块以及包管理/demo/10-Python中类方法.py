class Tool(object):
    # 定义一个类属性count
    count = 0

    # 定义一个__init__初始化方法
    def __init__(self, name):
        self.name = name
        Tool.count += 1

    # 封装一个类方法：专门实现对Tool.count类属性进行操作
    @classmethod
    def get_count(cls):
        print(f'我们使用Tool类共实例化了{cls.count}个工具')


t1 = Tool('斧头')
t2 = Tool('榔头')
t3 = Tool('铁锹')

Tool.get_count()