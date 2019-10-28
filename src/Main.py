# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 06:07:11 2019

@author: dmartinez

"""

from ProteinInfo import ProteinInfo as PInfo

"""""""""""""""""""""""""""""""""""

get_input_stream:
-----------------
    pFilePath = Should be the path to a file to be opened.

Description:
    Opens a file and gets its full stream of data
    
"""""""""""""""""""""""""""""""""""
def get_input_stream(pFilePath):
    try:   
        vFileObj = open(pFilePath, 'r')
        vFileContents = vFileObj.readlines()
        vFileObj.close()
        return vFileContents
    except FileNotFoundError:
        print("File could not be found or path doesn't exist. Try again.")
        return None

"""""""""""""""

MAIN

"""""""""""""""
vProteinInfoArray = [] #Array of ProteinInfo objects
vProteinInfoData = get_input_stream('cullpdb_pc30_res3.0_R1.0_d191017_chains18877.gz') #Hard coded filename for now but need to change this

for line in vProteinInfoData: #Go through each line in the file and fill the array
    vTmpProteinInfoObj = PInfo(line)
    if vTmpProteinInfoObj is not None:
        vProteinInfoArray.append(PInfo(line))
        
