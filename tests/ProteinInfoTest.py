# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 06:14:12 2019

@author: dmartinez
"""
import sys
sys.path.append('../')
import unittest
from src.ProteinInfo import ProteinInfo as pinfo
from src.ProteinInfo import HelixInfo as hinfo
class TestProteinInfoClass(unittest.TestCase):
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

class TestHelixInfoClass(unittest.TestCase):
    def test_get_serial(self):
        vTestHelix = hinfo('HELIX    7 H2B LYS B   42  GLN B   57  1                                  16    ')
        self.assertEqual('7', vTestHelix.g_serial)
    def test_get_helix_id(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual('1', vTestHelix.g_helix_id)
    def test_get_init_res_name(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual('ASN', vTestHelix.g_init_residue_name)
    def test_get_init_chain_id(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual('A', vTestHelix.g_init_chain_id)
    def test_get_init_seq_num(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual('5', vTestHelix.g_init_seq_num)
    def test_get_init_icode(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual('', vTestHelix.g_init_icode)
    def test_get_end_res_name(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual('GLN', vTestHelix.g_end_residue_name)
    def test_get_end_chain_id(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual('A', vTestHelix.g_end_chain_id)
    def test_get_end_seq_num(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual('21', vTestHelix.g_end_seq_num)
    def test_get_end_icode(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual('', vTestHelix.g_end_icode)
    def test_get_helix_class(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual(1, vTestHelix.g_helix_class)
    def test_get_comment(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual('', vTestHelix.g_comment)
    def test_get_length(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual(17, vTestHelix.g_length)
    def test_get_helix_1(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  1                                  17    ')
        self.assertEqual('Right-handed alpha', vTestHelix.get_helix_class())
    def test_get_helix_2(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  2                                  17    ')
        self.assertEqual('Right-handed omega', vTestHelix.get_helix_class())
    def test_get_helix_3(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  3                                  17    ')
        self.assertEqual('Right-handed pi', vTestHelix.get_helix_class())
    def test_get_helix_4(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  4                                  17    ')
        self.assertEqual('Right-handed gamma', vTestHelix.get_helix_class())
    def test_get_helix_5(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  5                                  17    ')
        self.assertEqual('Right-handed 3 - 10', vTestHelix.get_helix_class())
    def test_get_helix_6(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  6                                  17    ')
        self.assertEqual('Left-handed alpha', vTestHelix.get_helix_class())
    def test_get_helix_7(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  7                                  17    ')
        self.assertEqual('Left-handed omega', vTestHelix.get_helix_class())
    def test_get_helix_8(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  8                                  17    ')
        self.assertEqual('Left-handed gamma', vTestHelix.get_helix_class())    
    def test_get_helix_9(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21  9                                  17    ')
        self.assertEqual('27 Ribbon helix', vTestHelix.get_helix_class())
    def test_get_helix_10(self):
        vTestHelix = hinfo('HELIX    1   1 ASN A    5  GLN A   21 10                                  17    ')
        self.assertEqual('Polyproline', vTestHelix.get_helix_class())
if __name__ == '__main__':
    unittest.main()