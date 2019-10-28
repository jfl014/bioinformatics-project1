# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 05:55:44 2019

@author: dmartinez
"""

class ProteinInfo:
    g_pid = ''
    g_length = -1
    g_experimental = ''
    g_resolution = -1.0
    g_rfactor = -1.0
    g_freervalue = -1.0
    
    def __init__(self, pInput):
        # body of the constructor
        toks = pInput.split()
        try:
            self.g_pid = toks[0]
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