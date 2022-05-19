from randomwalk_2nd import RandomWalk2
import random
import matplotlib.pyplot as pl

'''setup the instance for random walk'''
random_walk_pic = RandomWalk2()
random_walk_pic.fill_walk()
random_walk_pic.get_steps()
while True:
    pl.style.use('seaborn')
    '''set the size of the fig and the pixel'''
    fig,ax = pl.subplots(figsize = (15,9), dpi= 128)

    '''point_number to set a range of number to align with the walk-steps that is to color the dot'''
    point_number = range(random_walk_pic.point_nums)

    ax.scatter(random_walk_pic.x_value, random_walk_pic.y_value, c = point_number, cmap=pl.cm.Blues, edgecolors = 'none',s = 10)

    '''if you want to enlighten the start and end point '''
    ax.scatter(0,0,c='red',s=100)
    ax.scatter(random_walk_pic.x_value[-1],random_walk_pic.y_value[-1],c='orange',s=50)

    '''You can hide the x-axis and y-axis'''
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    pl.show()
    '''make choice to re-walk or stop'''
    choice = input('Do you wanna another walk? (y/n) :' )
    if choice == 'n' or choice == 'N':
        break