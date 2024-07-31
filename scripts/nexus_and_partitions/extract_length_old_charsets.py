#!/usr/bin/env python

import fileinput
import os
import shutil
import argparse
from Bio import SeqIO, Nexus
#import warnings
#import time
#from nexus import NexusReader



## 2-Input parsing commands
parser=argparse.ArgumentParser(description="DESCRIPTION",formatter_class=argparse.RawTextHelpFormatter)

requiredName=parser.add_argument_group('required named arguments')
requiredName.add_argument("-p", "--path", required=True, 
			help="Path to directory with nexus files")

args=parser.parse_args()

## 3-Rename input parameters
path = os.path.join(os.getcwd(), args.path)
# get wd
current_wd = os.path.dirname(__file__)
diccionari = (".nex")
for file in os.listdir(path):
	file_path=os.path.join(path,file)
	if os.path.splitext(file_path)[1] in diccionari:
		for line in fileinput.input(file_path):
			start = "nchar"
			end = ";"
			if "nchar=" in line:
				line = str(line.split(start)[1].split(end)[0])
				# line=str(line.strip("charset"))
				# line=str(line.replace("MA =","MA = [").replace("TM =","TM = [").replace("IM =","IM = [").replace(";","]").replace(" ",",").replace(",=,","=").replace(",MA=[,","_MA=[").replace(",TM=[,","_TM=[").replace(",IM=[,","_IM=["))
				# line=str(line.replace(","," ").replace("-",","))
				file = str(file.replace("_nt_aligned.nex", "").replace(" ", ""))
				print(file + line, end='\n')
			else:
				continue
	else:
		continue

