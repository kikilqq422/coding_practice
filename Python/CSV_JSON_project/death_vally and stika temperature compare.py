import csv
import matplotlib.pyplot as pl
from datetime import datetime

''''!!! dates,high_tep,low_tep = [],[],[] should be setup individually or 
the latter one would contain the previous data
!!!! to get the column with the head row
    index = reader_head.index('TMAX') '''

filename_s = 'sitka_weather_2018_simple.csv'
filename_d = 'death_valley_2018_simple.csv'


def get_data(filename,high_tep,low_tep,dates):
    with open(filename) as f:
        reader = csv.reader(f)
        reader_head = next(reader)
        print(reader_head)
        '''!!!! to get the column with the head row'''
        n_1 = reader_head.index('TMAX')
        n_2 = reader_head.index('TMIN')
        n_d = reader_head.index('DATE')
        # n_1 = int(input('Please enter the column you\' like to excavate: '))
        # n_2 = int(input('Please enter the column you\' like to excavate: '))
        # n_d = int(input('Please enter the column you\' like to excavate: '))
        for row in reader:
            try:
                high = int(row[n_1])
                low = int(row[n_2])
                date = datetime.strptime(row[n_d], '%Y-%m-%d')
            except ValueError:
                print(f'Missing date for {date}')
            else:
                high_tep.append(high)
                low_tep.append(low)
                dates.append(date)
    return high_tep,low_tep,dates

'''TO DRAW PLOTS'''
pl.style.use('seaborn')
fig,ax =pl.subplots()


'''get data of temp in Stika
!!! dates,high_tep,low_tep = [],[],[] should be setup individually or 
the latter one would contain the previous data
'''

dates = []
high_tep = []
low_tep = []
S = get_data(filename_s,high_tep,low_tep,dates)
ax.plot(S[-1],S[0],c='red',alpha = 0.6)
ax.plot(S[-1],S[1],c='blue',alpha = 0.6)
ax.fill_between(S[2],S[0],S[1],facecolor = 'blue', alpha = 0.5)

'''GET DATA OF DEATH VALLY'''
dates = []
high_tep = []
low_tep = []
D = get_data(filename_d,high_tep,low_tep,dates)
ax.plot(D[-1],D[0],c='red',alpha = 0.2)
ax.plot(D[-1],D[1],c='blue',alpha = 0.2)
ax.fill_between(D[2],D[0],D[1],facecolor = 'blue', alpha = 0.15)

title = input('Please choose title for this plot: ')
pl.title(title, fontsize=20)
pl.xlabel(' ', fontsize=10)
pl.ylabel('Temperature(F)', fontsize=10)
pl.tick_params(axis='both', which='major', labelsize=20)
fig.autofmt_xdate()
pl.ylim(10,130)

pl.show()



