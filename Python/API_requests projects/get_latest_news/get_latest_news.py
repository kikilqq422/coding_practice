'''对hacker_new这个网站，通过调用API，查找其所有top-stories的查找ID
其中文章查阅的url设计为：https://hacker-news.firebaseio.com/v0/item/{id}.json'
通过 'https://hacker-news.firebaseio.com/v0/topstories.json'找到所有热门文章的id，并获取每个文章的内容
'''

import requests,json

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'the status code is {r.status_code}')
url_id = r.json()
filename = 'hacker_news_id.json'
with open(filename,'w') as f:
    json.dump(url_id,f,indent=4)

with open(filename) as f:
    content = json.load(f)
    print(f'get several id: {url_id[:10]}')
    print(f'There are {len(url_id)} top_stories on the face page')

'''Use each id to get every article by API'''
name = ['url'+str(i) for i in range(1,len(url_id))]
print(name)

url = str([i for i in url_id])
print(url)
for id_get in url_id[:10]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{id_get}.json'
    r = requests.get(url)
    content = r.json()
    print(f'the status_code is {r.status_code}')
    filename = f'hacker_news_{id_get}.json'
    with open(filename,'w') as f:
        json.dump(content,f,indent=4)
        # for key,value in content:
        comment_num = content['descendants']
        title = content['title']
        link = content['url']
        author = content['by']
        print(f'title:{title}\nlink:{link}\ncomments:{comment_num}')
