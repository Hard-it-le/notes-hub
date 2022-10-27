class Game(object):
    # 1、定义类属性top_score
    top_score = 0

    # 2、定义初始化方法__init__
    def __init__(self, player_name):
        self.player_name = player_name

    # 3、定义静态方法，用于输出帮助信息
    @staticmethod
    def show_help():
        print('游戏帮助信息')

    # 4、定义类方法
    @classmethod
    def show_top_score(cls):
        print(f'本游戏历史最高分：{cls.top_score}')

    # 5、定义实例方法，start_game()
    def start_game(self):
        print(f'{self.player_name}，游戏开始了，你准备好了么？')


# 实例化类生成实例对象
mario = Game('itheima')
mario.start_game()

# 显示历史最高分
Game.show_top_score()

# 弹出游戏帮助信息
Game.show_help()