import json
import pygal
import sys
sys.path.append(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization')
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code

# Load the data into a list.
filename = r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\csv_json_files\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

    # Print the 2010 population for each country.
    # Build a dictionary of population data for three categories of population size.
    cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}

    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                if population <= 10000000: #10,000,000
                    cc_pop_1[code] = population
                elif population <= 1000000000: #1,000,000,000
                    cc_pop_2[code] = population
                else:
                    cc_pop_3[code] = population

wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.value_formatter = lambda data: format(data, ',')
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)
wm.render_to_file(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\images\world_population.svg')