from roll_dice import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline
'''First chooce a dice with default size_num'''
dice_1 = Die()
# dice_1.roll_dice()

'''How many times do you wanna to roll the dice and put the result in record'''
num_roll = int(input('Please enter the rounds you like to play: '))
result = []
for num in range(num_roll+1):
    result.append(dice_1.roll_dice())
print(result)
print(result.count(1))
'''From the point your get for each roll, then count the frequencies of the result'''
frequencies = []
for point in range(1,dice_1.size_num+1):
    frequency = result.count(point)
    frequencies.append(frequency)

print(f'frequencies is {frequencies}, {max(frequencies)}')

'''visualize the result using histogram'''
'''Bar() collect data of x-axis and y axis to make histogram'''
x_value = list(range(1,dice_1.size_num+1))
data = [Bar(x=x_value, y=frequencies)]
'''each x/y axis can be setup individually, here are only add title to it'''
x_axis_config = {'title' : 'size_num'}
y_axis_config = {'title' : 'frequencies'}
my_layout = Layout(title='the frequency of roll dice', xaxis=x_axis_config,yaxis=y_axis_config)
'''offline.plot function to make histogram'''
offline.plot({'data':data, 'layout':my_layout}, filename='roll_dice.html')

