import json
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
import sys
sys.path.append(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization')
from country_codes import get_country_code

# Plot most recent year GDP data for all countries.

filename = r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\csv_json_files\world_gdp.json'
with open(filename) as f:
    data = json.load(f)

    # Lower, Middle, Upper GDP; Pygal automatically sorts data into three colored groups.
    global_gdp_1, global_gdp_2, global_gdp_3 = {}, {}, {}
    for datadict in data:
        if datadict['Year'] == 2016:
            country_name = datadict['Country Name']
            country_gdp = int(datadict['Value'])
    
            code = get_country_code(country_name)
            if code:
                if country_gdp <= 10000000000: # 10,000,000,000
                    global_gdp_1[code] = country_gdp
                elif country_gdp <= 100000000000: # 100,000,000,000
                    global_gdp_2[code] = country_gdp
                else:
                    global_gdp_3[code] = country_gdp

wm = pygal.maps.world.World()
wm.title = "Gross Domestic Product of All Countries (2016)"
wm.value_formatter = lambda data: format(data, ',')
wm.add('<= 10b GDP', global_gdp_1)
wm.add('<= 100b GDP', global_gdp_2)
wm.add('> 100b GDP', global_gdp_3)
wm.render_to_file(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\images\16_6.svg')