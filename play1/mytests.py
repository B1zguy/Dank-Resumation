import unittest
from first_iter import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hellow_world(), 'hello world')

    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)