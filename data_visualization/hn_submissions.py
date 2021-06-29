import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
#print(f'Status Code: {r.status_code}')

r_dict = r.json()

submissions = []
for id_num in r_dict[:30]:
    url_link = f'https://hacker-news.firebaseio.com/v0/item/{id_num}.json/'
    new_r = requests.get(url_link)        
    dicts = new_r.json()
    submission = {
        'title': dicts['title'],
        'link': f'http://hacker-news.firebaseio.com/item?={dicts["id"]}',
        'total_comments': dicts.get('descendants', 0)
        }
    submissions.append(submission)
    submissions = sorted(submissions, key=itemgetter('total_comments'), reverse=True)

for post_dict in submissions:
    print('\n')
    print(f'Title: {post_dict["title"]}')
    print(f'URL: {post_dict["link"]}')
    print(f'Comments: {post_dict["total_comments"]}')