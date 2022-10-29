# 定义一个播放器类
class MusicPlayer(object):
    # 定义一个类属性，如instance，用于记录之前实例化对象返回的内存引用
    instance = None
    # 重写__new__()魔术方法
    def __new__(cls, *args, **kwargs):
        # 判断实例化时有没有分配过内存空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name

# 1、实例mp1对象
mp1 = MusicPlayer('红色的高跟鞋')
print(mp1)

# 2、实例化mp2对象
mp2 = MusicPlayer('春夏秋冬')
print(mp2)