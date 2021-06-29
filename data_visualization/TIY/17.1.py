import requests
import pygal
import time
from pygal.style import Style
from datetime import datetime
from os import path

languages = ['javascript', 'ruby', 'c', 'java', 'perl', 'haskell', 'go']

for language in languages:

    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
    r = requests.get(url)
    r_dict = r.json()

    repo_info_list = []
    repo_names = []

    try:
        for repo in r_dict['items']:
            repo_info = {
                'label': str(repo['description']), # IF NONETYPE, CONVERT NONE boolean TO 'NONE' string.'
                                                   # emojis are converted to strings
                'value': repo['stargazers_count'],
                'xlink': repo['html_url']
                }

            repo_info_list.append(repo_info)
            repo_names.append(repo['name'])
    except KeyError:
        url = 'https://api.github.com/rate_limit'
        r = requests.get(url)

        rate_limit_dicts = r.json()
        rate_limit = rate_limit_dicts['resources']['search']['limit']
        remaining_limit = rate_limit_dicts['resources']['search']['remaining']

        epoch_reset_time = rate_limit_dicts['resources']['search']['reset']
        current_epoch_time = time.time()
        seconds_since = str(int(epoch_reset_time - current_epoch_time))

        print(
        f'\nPlease wait {seconds_since} seconds for limit reset.\n\n{url}\nRate Limit: {rate_limit}',
        f'\nRemaining Limit: {remaining_limit}',
        )
        break

    my_style = Style(
        title_font_size = 50,
        label_font_size = 25,
        major_label_font_size = None,
        y_title = 'Amount of Stars',
        tooltip_font_size = 30
        )

    if language == 'javascript':
        language_str = 'JavaScript'
    else:
        language_str = language.title()
    
    bar = pygal.Bar(show_legend=False, style=my_style)
    bar.width, bar.height = 2000, 1250
    date = str(datetime.now())
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    date = datetime.strftime(date, f'%B %d, %Y // %I:%M:%S')
    bar.title = f'Most Popular Repositories in {language_str}\n*as of {date}.'
    bar.add('', repo_info_list)
    bar.value_formatter = lambda data: format(int(data), ',') # dont have a solid foundation of understanding this
    bar.x_labels = repo_names
    bar.x_label_rotation = 45

    filename = fr'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\images\17_1-{language_str}.svg'
    if path.exists(filename):
        print(f'Updated File: 17_1-{language_str}.svg')
    else:
        print(f'Created File: 17_1-{language_str}.svg')
    
    bar.render_to_file(filename)