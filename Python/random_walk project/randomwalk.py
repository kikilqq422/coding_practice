import random
class RandomWalk:
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
            self.x_direction = random.choice([1,-1])
            self.x_distance = random.choice([0,1,2,3,4])

            self.x_steps = self.x_direction * self.x_distance

            self.y_direction = random.choice([1,-1])
            self.y_distance = random.choice([0,1, 2, 3, 4])

            self.y_steps = self.y_direction * self.y_distance

            '''if the x,y combined move is 0, it should be stooped'''
            if self.x_steps == 0 and self.y_steps == 0:
                continue

            '''the value of the next'''
            x = self.x_value[-1] + self.x_steps
            y = self.y_value[-1] + self.y_steps
            self.x_value.append(x)
            self.y_value.append(y)


