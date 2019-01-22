# coding:utf-8

# 实例方法：内部需要使用实例属性
# 类方法：内部只需访问类属性
# 静态方法，不需要访问实例和类属性


class Game(object):

    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    # 静态方法
    @staticmethod
    def show_help():
        print 'help info'

    # 类方法
    @classmethod
    def show_top_score(cls):
        print 'histrical top score %d' % Game.top_score

    def start_game(self):
        print '%s start the game' % self.player_name


# help information
Game.show_help()

# hiostry score
Game.show_top_score()

# game player
game = Game('xiaoming')
game.start_game()