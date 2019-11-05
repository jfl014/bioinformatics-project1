# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 06:07:11 2019

@author: dmartinez

"""

from ProteinInfo import ProteinInfo as PInfo
from ProteinInfo import HelixInfo as HInfo
import urllib.request

"""""""""""""""""""""""""""""""""""

get_input_stream:
-----------------
    pFilePath = Should be the path to a file to be opened.
    
    Example: 
        -'C:\Local\Path\SomeFile.txt'

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

"""""""""""""""""""""""""""""""""""

get_input_stream_url_lib:
-----------------
    pUrl = Url of the file to be downloaded
    pPdbId = PID filename of a file on the Protein Databank
    
    Examples: 
        -'https://files.rcsb.org/download/'
        -'3UTS.pdb'

Description:
    Attempts to retrieve the file at the specified url and
    opens the file then returns its input stream.
    
"""""""""""""""""""""""""""""""""""
def get_input_stream_url_lib(pUrl, pPdbId):
    try:
        vPdbFileObj = urllib.request.urlretrieve(pUrl+pPdbId, pPdbId)
        return get_input_stream(pPdbId)
    except urllib.error.HTTPError:
        print("Url could not be found.")
        return None

"""""""""""""""

MAIN

"""""""""""""""
g_BASE_URL = 'https://files.rcsb.org/download/'
vProteinInfoArray = [] #Array of ProteinInfo objects
vProteinInfoData = get_input_stream('cullpdb_pc30_res3.0_R1.0_d191017_chains18877.gz') #Hard coded filename for now but need to change this

for line in vProteinInfoData: #Go through each line in the file and fill the array
    vTmpProteinInfoObj = PInfo(line)
    if vTmpProteinInfoObj.g_pid is not None:
        vProteinInfoArray.append(PInfo(line))

#for protein in vProteinInfoArray: #Get the specified proteins from the databank
 #   get_input_stream_url_lib(g_BASE_URL, str(protein.g_pid)+".pdb")

vHelixCount = [0,0,0,0,0,0,0,0,0,0]
vHelixArray = []
 
for protein in vProteinInfoArray:
    vProteinFileStream = get_input_stream(protein.g_pid+".pdb")
    if vProteinFileStream is not None:
        for line in vProteinFileStream:
            if line.startswith("HELIX "):
                vHelixArray.append(HInfo(line))

for helix in vHelixArray:
    try:
        vHelixCount[helix.g_helix_class-1] += 1
    except:
        print("Bad Helix Class: " + str(helix.g_helix_class))

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
        
helix_names = ['Right-handed alpha', 'Right-handed omega', 'Right-handed pi',
               'Right-handed gamma', 'Right-handed 3 - 10', 'Left-handed alpha',
               'Left-handed omega', 'Left-handed gamma', '27 Ribbon helix',
               'Polyproline']

print("Total amount of helices: " + str(len(vHelixArray)))

i = 0
for helix in vHelixCount:
    percentage = helix / len(vHelixArray)
    print(helix_names[i] + ": " + str(helix) + " / " + str(len(vHelixArray)) + " (" + str(round(percentage*100, 3)) + "% of data set)")
    i += 1