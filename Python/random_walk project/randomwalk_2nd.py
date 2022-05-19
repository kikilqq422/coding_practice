import random
class RandomWalk2:
    def __init__(self, point_nums = 5000):
        '''choice the total wolk-steps'''
        self.point_nums = point_nums
        '''choice a starting point, start with (0,0)'''
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        '''walk until the final walks'''
        while len(self.x_value) < self.point_nums:
            '''choice the direction and set the steps'''
            x_steps = self.get_steps()
            y_steps = self.get_steps()


            '''if the x,y combined move is 0, it should be stopped'''
            if x_steps == 0 and y_steps == 0: continue

            '''the value of the next'''
            x = self.x_value[-1] + x_steps
            y = self.y_value[-1] + y_steps
            self.x_value.append(x)
            self.y_value.append(y)

    def get_steps(self):
        direction = random.choice([1, -1])
        distance = random.choice([0, 1, 2, 3, 4])

        steps = direction * distance
        return steps
