import requests
import pygal
import datetime
from operator import itemgetter
from timeit import default_timer as timer

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
r_dict = r.json()

r_dict_total_info = []
for id_num in r_dict[:30]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{id_num}.json'
    r = requests.get(url)
    r_dict = r.json()
    
    r_dict_info = {
        'label': r_dict['title'],
        'value': r_dict['descendants'],
        'xlink': f'https://news.ycombinator.com/item?id={id_num}',
        }
    
    r_dict_total_info.append(r_dict_info)
    r_dict_total_info = sorted(r_dict_total_info, key=itemgetter('value'), reverse=True)

bar = pygal.Bar(show_legend=False, truncate_legend=-1, width=1200)

date = datetime.datetime.now() # 2019-12-21 09:40:49.794287
date = datetime.datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S.%f')
date = datetime.datetime.strftime(date, '%B %d, %Y %I:%M:%S %p') # December 21, 2019 09:52:31 AM
bar.title = f'Most Active 30 Articles on HackerNews (Page 1) \n {date}'

bar.add('', r_dict_total_info)

bar.render_to_file(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\images\17_2.svg')