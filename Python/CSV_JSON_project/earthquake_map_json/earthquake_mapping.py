import json
import plotly.express as px
import pandas as pd

filename = 'eq_data_1_day_m1.json'
with open(filename) as f:
    content = json.load(f)
    # print(content)

file_save = 'file_save_1_day.json'
with open(file_save,'w') as f1:
    json.dump(content,f1,indent=4)
'''extract data from json'''
with open(file_save) as f2:
    content_all = json.load(f2)
    all_data = content_all['features']
    print(all_data[:3])
    titles,mags,longs,latis = [],[],[],[]
    for data in all_data:
        mag = data['properties']['mag']
        title = data['properties']['title']
        long = data['geometry']['coordinates'][0]
        lati = data['geometry']['coordinates'][1]
        mags.append(mag)
        titles.append(title)
        longs.append(long)
        latis.append(lati)

    print(mags[:10],titles[:5],longs[:5],latis[:5])

'''draw scatter using plotpy.express'''
plot = pd.DataFrame(
    data = zip(mags,titles,longs,latis), columns = ['magnitudes','locations','longitudes','latitudes']
)
plot.head()

fig = px.scatter(
    plot,
    x = longs,
    y = latis,
    labels={'x':'longitude',
            'y':'latitude'},
    range_x=[-200,200],
    range_y=[-90,90],
    width = 800,
    height = 800,
    title = 'scatter of global earthquake point',
    size = 'magnitudes',
    size_max = 10,
    color = 'magnitudes',
    hover_name = 'locations',
)
fig.write_html('global earthquake.html')
# fig.show()







