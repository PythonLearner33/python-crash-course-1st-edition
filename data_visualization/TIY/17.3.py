import sys
sys.path.append(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization')
from python_repos import r, response_dict
import unittest

class test_python_repos(unittest.TestCase):
    def test(self):
        self.assertEqual(r.status_code, 200)
        self.assertNotEqual(r.status_code, None)
        self.assertGreater(int(response_dict['total_count']), 1)
        self.assertNotEqual(int(response_dict['total_count']), None)

unittest.main()