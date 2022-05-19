'''extract the dates and raindrops amount from Stika and Death valley to draw plots'''

import csv
import matplotlib.pyplot as pl
from datetime import datetime

filename = 'sitka_weather_2018_simple.csv'
filename_deathvalley = 'death_valley_2018_simple.csv'
dates = []
wet = []
wet_d = []

with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    for row in reader:
        try:
            '''注意如果不加入float, row[3]取出来直接为string'''
            date_format = datetime.strptime(str(row[2]), '%Y-%m-%d')
            print(date_format)
        except ValueError:print(f'{dates} is missing')
        else:
            dates.append(date_format)
            wet.append(float(row[3]))

with open(filename_deathvalley) as f_d:
    reader_d = csv.reader(f_d)
    head_row_d = next(reader_d)
    print(head_row_d)
    for content in reader_d:
        wet_d.append(float(content[3]))

print('dates:',len(dates),'wet_d:',len(wet_d))
wet_d = wet_d[:-1]
pl.style.use('seaborn')
fig,ax = pl.subplots()
# ax.plot(dates, wet, c='blue')
ax.plot(dates, wet_d, c='red')

'''设置图形格式'''
pl.title('Daily raindrops amounts-2018',fontsize = 24)
pl.xlabel('Date', fontsize = 10)
pl.ylabel('humidity amount', fontsize = 10)
pl.tick_params(axis='both', which = 'major', labelsize=16)
'''set the range of x_axis and y_axis'''
pl.ylim(0,0.5)
# pl.xlim('2018-01-01 ','2019-01-01')
pl.show()