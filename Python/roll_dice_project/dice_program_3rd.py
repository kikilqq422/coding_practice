'''here is to take 3 dices and its result frequencies'''
from roll_dice import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

'''First chooce a dice with default size_num'''
dice_1 = Die(6)
# dice_1.roll_dice()
dice_2 = Die(6)
dice_3 = Die(6)

'''How many times do you wanna to roll the dice and put the result in record'''
num_roll = int(input('Please enter the rounds you like to play: '))
result = []
max_sizes = dice_1.size_num + dice_2.size_num + dice_3.size_num

'''when increase the '''
for each_roll in range(num_roll):
    result_dice = dice_1.roll_dice() + dice_2.roll_dice() + dice_3.roll_dice()
    result.append(result_dice)
print(len(result))

'''From the point your get for each roll, then count the frequencies of the result'''
frequencies = []
for point in range(3,max_sizes+1):
    frequency = result.count(point)
    frequencies.append(frequency)

print(f'frequencies is {frequencies}, {max(frequencies)}')

'''visualize the result using histogram'''
'''Bar() collect data of x-axis and y axis to make histogram'''
x_value = list(range(3,max_sizes))
data = [Bar(x=x_value, y=frequencies)]
'''each x/y axis can be setup individually, here are only add title to it'''
x_axis_config = {'title' : 'size_num'}
y_axis_config = {'title' : 'frequencies'}
my_layout = Layout(title='the frequency of roll dice', xaxis=x_axis_config,yaxis=y_axis_config)
'''offline.plot function to make histogram'''
offline.plot({'data':data, 'layout':my_layout}, filename='roll_dice_3.html')

