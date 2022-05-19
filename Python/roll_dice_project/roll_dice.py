'''创建一个掷筛在的类'''
from random import randint
class Die:
    def __init__(self, size_num = 6):
        self.size_num = size_num

    '''every time you get a random point of a dice'''
    def roll_dice(self):
        # print(f'You got a {randint(1,self.size_num)}')
        return randint(1,self.size_num)
