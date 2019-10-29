# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 06:14:12 2019

@author: dmartinez
"""
import sys
sys.path.append('../')
import unittest
from src.ProteinInfo import ProteinInfo as pinfo

class TestStringMethods(unittest.TestCase):
    def test_get_pid(self):
        vTestProtein = pinfo('12ASA       330  XRAY        2.200    0.16    0.29')
        self.assertEqual('12AS', vTestProtein.g_pid)
    def test_get_pid2(self):
        vTestProtein = pinfo('12ASA       330  XRAY        2.200    0.16    0.29')
        self.assertEqual('A', vTestProtein.g_chain)
    def test_get_length(self):
        vTestProtein = pinfo('12ASA       330  XRAY        2.200    0.16    0.29')
        self.assertEqual(330, vTestProtein.g_length)
    def test_get_experimental(self):
        vTestProtein = pinfo('12ASA       330  XRAY        2.200    0.16    0.29')
        self.assertEqual('XRAY', vTestProtein.g_experimental)
    def test_get_resolution(self):
        vTestProtein = pinfo('12ASA       330  XRAY        2.200    0.16    0.29')
        self.assertEqual(2.200, vTestProtein.g_resolution)
    def test_get_rfactor(self):
        vTestProtein = pinfo('12ASA       330  XRAY        2.200    0.16    0.29')
        self.assertEqual(0.16, vTestProtein.g_rfactor)
    def test_get_freervalue(self):
        vTestProtein = pinfo('12ASA       330  XRAY        2.200    0.16    0.29')
        self.assertEqual(0.29, vTestProtein.g_freervalue)
    def test_invalid_data(self):
        vTestProtein = pinfo('PIDs         length Exptl.  resolution  R-factor FreeRvalue')
        self.assertIsNone(vTestProtein.g_pid)
        self.assertIsNone(vTestProtein.g_length)
        self.assertIsNone(vTestProtein.g_experimental)
        self.assertIsNone(vTestProtein.g_resolution)
        self.assertIsNone(vTestProtein.g_rfactor)
        self.assertIsNone(vTestProtein.g_freervalue)

        
if __name__ == '__main__':
    unittest.main()