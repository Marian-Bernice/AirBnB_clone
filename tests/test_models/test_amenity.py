#!/usr/bin/python3
"""Test User Class - Comproving expectect outputs and documentation
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    this class test Amenity class and your behavior
    """

    def setUp(self):
        self.amenity = Amenity()

    def test_creation(self):
        '''this test validate that creation proccess was correct.
        '''
        self.assertEqual(self.amenity.name, '')
