# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 05:55:44 2019

@author: dmartinez
"""
import sys

class ProteinInfo:
    g_pid = ''
    g_chain = ''
    g_length = -1
    g_experimental = ''
    g_resolution = -1.0
    g_rfactor = -1.0
    g_freervalue = -1.0
    
    def __init__(self, pInput):
        # body of the constructor
        toks = pInput.split()
        try:
            self.g_pid = toks[0][:-1]
            self.g_chain = toks[0][-1:]
            self.g_length = int(toks[1])
            self.g_experimental = toks[2]
            self.g_resolution = float(toks[3])
            self.g_rfactor = float(toks[4])
            self.g_freervalue = float(toks[5])
        except:
            self.g_pid = None
            self.g_length = None
            self.g_experimental = None
            self.g_resolution = None
            self.g_rfactor = None
            self.g_freervalue = None
            
class HelixInfo:
    g_serial = -1 #Serial Number of the helix. Starts at 1 and increases incrementally
    g_helix_id = -1 #Helix Identifier. Alphanumeric
    g_init_residue_name = '' #Name of the initial residue
    g_init_chain_id = '' #Chain identifier for the chain containing this helix
    g_init_seq_num = -1 #Sequence number of the initial residue
    g_init_icode = -1 #Insertion code of the initial residue
    g_end_residue_name = '' #Name of terminal residue of the helix
    g_end_chain_id = '' #chain identifier for the chain containing this helix
    g_end_seq_num = -1 #Sequence number of the terminal residue
    g_end_icode = -1 #Insertion code of the terminal residue
    g_helix_class = '' #Helix class
    g_comment = '' #Comment
    g_length = -1 #length of this helix
    
    def __init__(self, pInput):
        # body of the constructor
        toks = pInput.split()
        try:
            self.g_serial = pInput[7:10].replace(' ', '')
            self.g_helix_id = pInput[11:14].replace(' ', '')
            self.g_init_residue_name = pInput[15:18].replace(' ', '')
            self.g_init_chain_id = pInput[19].replace(' ', '')
            self.g_init_seq_num = pInput[21:25].replace(' ', '')
            self.g_init_icode = pInput[25].replace(' ', '')
            self.g_end_residue_name = pInput[27:30].replace(' ', '')
            self.g_end_chain_id = pInput[31].replace(' ', '')
            self.g_end_seq_num = pInput[33:37].replace(' ', '')
            self.g_end_icode = pInput[37].replace(' ', '')
            self.g_helix_class = int(pInput[38:40].replace(' ', ''))
            self.g_comment = pInput[40:70].replace(' ', '')
            self.g_length = int(pInput[71:76].replace(' ', ''))
        except:
            self.g_serial = None
            self.g_helix_id = None
            self.g_init_residue_name = None
            self.g_init_chain_id = None
            self.g_init_seq_num = None
            self.g_init_icode = None
            self.g_end_residue_name = None
            self.g_end_chain_id = None
            self.g_end_seq_num = None
            self.g_end_icode = None
            self.g_helix_class = None
            self.g_comment = None
            self.g_length = None
            print(sys.exc_info()[0])
    
    def get_helix_class(self):
        vRIGHT_HANDED_ALPHA = 1
        vRIGHT_HANDED_OMEGA = 2
        vRIGHT_HANDED_PI = 3
        vRIGHT_HANDED_GAMMA = 4
        vRIGHT_HANDED_310 = 5
        vLEFT_HANDED_ALPHA = 6
        vLEFT_HANDED_OMEGA = 7
        vLEFT_HANDED_GAMMA = 8
        v27_RIBBON_HELIX = 9
        vPOLYPROLINE = 10
        
        if self.g_helix_class == vRIGHT_HANDED_ALPHA:
            return 'Right-handed alpha'
        elif self.g_helix_class == vRIGHT_HANDED_OMEGA:
            return 'Right-handed omega'
        elif self.g_helix_class == vRIGHT_HANDED_PI:
            return 'Right-handed pi'
        elif self.g_helix_class == vRIGHT_HANDED_GAMMA:
            return 'Right-handed gamma'
        elif self.g_helix_class == vRIGHT_HANDED_310:
            return 'Right-handed 3 - 10'
        elif self.g_helix_class == vLEFT_HANDED_ALPHA:
            return 'Left-handed alpha'
        elif self.g_helix_class == vLEFT_HANDED_OMEGA:
            return 'Left-handed omega'
        elif self.g_helix_class == vLEFT_HANDED_GAMMA:
            return 'Left-handed gamma'
        elif self.g_helix_class == v27_RIBBON_HELIX:
            return '27 Ribbon helix'
        elif self.g_helix_class == vPOLYPROLINE:
            return 'Polyproline'
        else:
            return None