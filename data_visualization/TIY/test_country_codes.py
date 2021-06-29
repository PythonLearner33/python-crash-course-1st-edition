import unittest
import sys
sys.path.append(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization')
from country_codes import get_country_code
from pygal.maps.world import COUNTRIES

class WorldGDPTest(unittest.TestCase):
    '''Tests 16.6.py World GDP (2016).'''
    def test_16_6(self):
        
        # [Country Codes List]:
        # pygal.org/en/stable/documentation/types/maps/pygal_maps_world.html
        # -- same as pygal.maps.world.COUNTRIES // returns dictionary of code:country
        
        # If-statement Test (from COUNTRIES)
        self.assertEqual(get_country_code('Bolivia, Plurinational State of'), 'bo')
        self.assertEqual(get_country_code('Congo, the Democratic Republic of the'), 'cd')
        self.assertEqual(get_country_code('Libyan Arab Jamahiriya'), 'ly')
        self.assertEqual(get_country_code('Zimbabwe'), 'zw') # Titlecase test
        self.assertEqual(get_country_code('zimbabwe'), 'zw') # Lowercase test
        self.assertEqual(get_country_code('ZIMBABWE'), 'zw') # Uppercase test
        self.assertEqual(get_country_code('ZImbabWE'), 'zw') # Weirdcase test

        # Else-statement Test (from unlisted_countries)
        self.assertEqual(get_country_code('Bolivia'), 'bo')
        self.assertEqual(get_country_code('Congo, Dem. Rep.'), 'cd')
        self.assertEqual(get_country_code('Libya'), 'ly') # Titlecase test
        self.assertEqual(get_country_code('libya'), 'ly') # Lowercase test
        self.assertEqual(get_country_code('LIBYA'), 'ly') # Uppercase test
        self.assertEqual(get_country_code('LibYA'), 'ly') # Weirdcase test

unittest.main()
