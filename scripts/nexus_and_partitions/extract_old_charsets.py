#!/usr/bin/env python

import fileinput
import os
import shutil
import argparse
from Bio import SeqIO, Nexus
import pandas as pd
import warnings
import time



## 2-Input parsing commands
parser=argparse.ArgumentParser(description="DESCRIPTION",formatter_class=argparse.RawTextHelpFormatter)

requiredName=parser.add_argument_group('required named arguments')
requiredName.add_argument("-p", "--path", required=True, 
			help="Path to directory with fasta files")

args=parser.parse_args()

## 3-Rename input parameters
path=os.path.join(os.getcwd(),args.path)
# get wd
current_wd=os.path.dirname(__file__)
diccionari=(".nex");
for file in os.listdir(path):
	if os.path.splitext(os.path.join(path,file))[1] in diccionari:
		for line in fileinput.input(os.path.join(path,file)):
			if "charset" in line:
				line=str(line.strip("charset"))
				line=str(line.replace("MA =","MA = [").replace("TM =","TM = [").replace("IM =","IM = [").replace(";","]").replace(" ",",").replace(",=,","=").replace(",MA=[,","_MA=[").replace(",TM=[,","_TM=[").replace(",IM=[,","_IM=["))
				file=str(file.replace("_nt_aligned.nex","").replace(" ",""))
				print(file+line,end = ' ')
			else:continue
	else:continue
