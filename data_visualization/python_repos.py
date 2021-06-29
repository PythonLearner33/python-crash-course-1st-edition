import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from pygal.util import truncate

# Make an API call and store the response.
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
#print(f'\nStatus code: {r.status_code}')

# Store API response in a variable.
response_dict = r.json()
#print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    descriptions = repo_dict['description']

    if not descriptions:
        descriptions = 'No description provided.'
    else:
        words = descriptions.split()
        if len(words) > 15:
            words.insert(int(len(words)/2), '\n')
            descriptions = ' '.join(words)
    
    plot_dict = {
        'label': descriptions,
        'value': repo_dict['stargazers_count'],
        #'xlink': repo_dict['html_url'] ***Same as below. Idiot.***
        'xlink': {
            'href': repo_dict['html_url'],
            'target': '_blank'}
        }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14

my_config = pygal.Config()
my_config.show_legend = False
my_config.show_y_guides = True
my_config.y_labels_major_every = -1
my_config.x_label_rotation = 45
my_config.truncate_label = 15 # Shortens x-label only to 15 characters.
my_config.width = 1250
my_config.tooltip_border_radius = 10
my_config.value_formatter = lambda data: format(int(data), ',') # Add commas to numbers.

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.add('', plot_dicts)
chart.x_labels = names
chart.render_to_file('C:/Users/Alvin/Desktop/Desktop/python_work/Projects/data_visualization/images/python_repos.svg')