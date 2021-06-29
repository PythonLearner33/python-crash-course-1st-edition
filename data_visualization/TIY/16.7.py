import csv
import pygal
import sys
sys.path.append(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization')
from pygal.maps.world import COUNTRIES
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from country_codes import get_country_code, unlisted_countries
from check_gdp_tier import check_gdp_tier

filename = r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\csv_json_files\world_gdp_2018.csv'
with open (filename) as f:
    data = csv.reader(f)

    # Skips 5 lines down in csv file to get header.
    for i in range(5):
        header = next(data)

    # Data extraction for 2019.
    GDP_T1, GDP_T2, GDP_T3 = {}, {}, {}
    for index, row in enumerate(data):
        country_name = row[0]
        cc = get_country_code(country_name)
        try:
            # Make into a float, then int. Ex: 1.05751E+11 -> 105751000000.0 -> 105751000000
            gdp_2019 = int(float(row[62]))
        except ValueError:
            #print(f'Error: Line {index}, {row}.')
            pass
        else:
            check_gdp_tier(cc, gdp_2019, GDP_T1, GDP_T2, GDP_T3)

wm = pygal.maps.world.World()

wm.title = 'World GDP (2019)'
wm.value_formatter = lambda data: format(data, ',')

wm.add('<= 10B', GDP_T1)
wm.add('<= 100B', GDP_T2)
wm.add('> 100B', GDP_T3)

wm.render_to_file(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\images\16_7.svg')