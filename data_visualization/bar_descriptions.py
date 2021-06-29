import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#336699', basetyle=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = True
my_config.width = 1000

bar = pygal.Bar(config=my_config, style=my_style)
bar.title = 'Python Projects'
bar.x_labels = ['httpie', 'django', 'flask']
plot_dicts = [
    {'value':16101, 'label':'Description of httpie'},
    {'value':15028, 'label':'Description of django'},
    {'value':14798, 'label':'Description of flask'}
]
bar.add('', plot_dicts)
bar.render_to_file(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\images\bar_descriptions.svg')