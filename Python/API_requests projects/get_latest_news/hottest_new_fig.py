from plotly.graph_objs import Bar
from plotly import offline

'''对hacker_new这个网站，通过调用API，查找其所有top-stories的查找ID
其中文章查阅的url设计为：https://hacker-news.firebaseio.com/v0/item/{id}.json'
通过 'https://hacker-news.firebaseio.com/v0/topstories.json'找到所有热门文章的id，并获取每个文章的内容
'''

import requests,json
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
# print(f'the status code is {r.status_code}')
url_id = r.json()

'''Use each id to get every article by API
create a dict to include title,url,comments in it 
itemgetter could let the article ranking from your side of choice, like the comments section.
'''

url_dicts = []
url_dict = {}
# authors, links, comments,labels,links_click = [], [], [],[],[]
for id_get in url_id[:20]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{id_get}.json'
    r = requests.get(url)
    content = r.json()
    # print(f'the status_code is {r.status_code}')
    try:
        url_dict = {
        'comment_num': content['descendants'],
        'author' : content['by'],
        'title' : content['title'],
        'link' : content['url'],
        'label' : f"{content['comment_num']}<br \>{content['author']}<br \>{content['title']}",
        'link_click' : f"<a href = '{content['link']}'>{content['author']}</a>",
        }
        url_dicts.append(url_dict)
        print(url_dicts[:10])
        # print(f'title:{title}\nlink:{link}\ncomments:{comment_num}')
        # url_dicts.append(url_dict)
        # '''rank by comment_num'''
        # url_dicts = sorted(url_dicts,key=itemgetter('comment_num'),reverse=True)
        # print(url_dicts)
        # print(url_dicts['author'])
        # label = f"{url_dict['comment_num']}<br \>{url_dict['author']}<br \>{url_dict['title']}"
        # link_click = f"<a href = '{url_dict['link']}'>{url_dict['author']}</a>",
    except KeyError:
        print('some keys are missing')


        '''rank by comment_num'''
        url_dicts = sorted(url_dicts,key=itemgetter('comment_num'),reverse=True)
        print(url_dicts[:10])
            # print(url_dicts['author'])



#
# '''Visualize the lastest news '''
# data = [{
#     'type':'bar',
#     'x': url_dicts['author'],
#     'y':url_dicts['comment_num'],
#     'hovertext':url_dicts['label'],
# }]
# my_layout = {
#     'title':'The lastest news',
#     'xaxis':{'title':'news'},
#     'yaxis':{'title':'comments'},
# }
# fig = {
#     'data': data,
#     'layout': my_layout,
# }
# # # fig.autofmt_xdate()
# offline.plot(fig, filename='latest_news.html')
