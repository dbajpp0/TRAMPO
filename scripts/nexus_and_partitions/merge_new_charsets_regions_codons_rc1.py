#!/usr/bin/env python

import fileinput
import os
import argparse
import re

#INPUT DATA
parser=argparse.ArgumentParser(description="DESCRIPTION",formatter_class=argparse.RawTextHelpFormatter)

requiredName=parser.add_argument_group('required named arguments')
requiredName.add_argument("-a", "--file_new_charsets", required=True, 
			help="Path to directory with fasta files")

args=parser.parse_args()

## Rename input parameters
new=args.file_new_charsets

### Define lists

genes=("atp6","atp8","cob","cox1","cox2","cox3","nd1","nd2","nd3","nd4","nd5","nd6","ndl")

partitions=("charset updated_atp6_MA","charset updated_atp6_TM","charset updated_atp6_IM","charset updated_atp8_MA","charset updated_atp8_TM","charset updated_atp8_IM","charset updated_cob_MA","charset updated_cob_TM","charset updated_cob_IM","charset updated_cox1_MA","charset updated_cox1_TM","charset updated_cox1_IM","charset updated_cox2_MA","charset updated_cox2_TM","charset updated_cox2_IM","charset updated_cox3_MA","charset updated_cox3_TM","charset updated_cox3_IM","charset updated_nd1_MA","charset updated_nd1_TM","charset updated_nd1_IM","charset updated_nd2_MA","charset updated_nd2_TM","charset updated_nd2_IM","charset updated_nd3_MA","charset updated_nd3_TM","charset updated_nd3_IM","charset updated_nd4_MA","charset updated_nd4_TM","charset updated_nd4_IM","charset updated_nd5_MA","charset updated_nd5_TM","charset updated_nd5_IM","charset updated_nd6_MA","charset updated_nd6_TM","charset updated_nd6_IM","charset updated_ndl_MA","charset updated_ndl_TM","charset updated_ndl_IM")

MA=("charset updated_atp6_MA","charset updated_atp8_MA","charset updated_cob_MA ","charset updated_cox1_MA","charset updated_cox2_MA","charset updated_cox3_MA","charset updated_nd1_MA","charset updated_nd2_MA","charset updated_nd3_MA","charset updated_nd4_MA","charset updated_nd5_MA","charset updated_nd6_MA","charset updated_ndl_MA")

TM=("charset updated_atp6_TM","charset updated_atp8_TM","charset updated_cob_TM ","charset updated_cox1_TM","charset updated_cox2_TM","charset updated_cox3_TM","charset updated_nd1_TM","charset updated_nd2_TM","charset updated_nd3_TM","charset updated_nd4_TM","charset updated_nd5_TM","charset updated_nd6_TM","charset updated_ndl_TM")

IM=("charset updated_atp6_IM","charset updated_atp8_IM","charset updated_cob_IM ","charset updated_cox1_IM","charset updated_cox2_IM","charset updated_cox3_IM","charset updated_nd1_IM","charset updated_nd2_IM","charset updated_nd3_IM","charset updated_nd4_IM","charset updated_nd5_IM","charset updated_nd6_IM","charset updated_ndl_IM")

print('#nexus')
print('begin sets;')

#DEFINE SET AM_cod1
print("\tcharset MA_cod1 =", sep=' ', end='', flush=True)
f = open(new, "r")
for line in f:
	line=line.replace('\t','')
	if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
	#print(line,end = ' ')
		if "_MA_cod1" in line:
			for word in genes:
				if word in line:
					#print(word)
					line=line.replace("\n","").replace(word,"").replace("=","").replace(";","").replace("charset","").replace("updated_","").replace("_cod1","").replace("_cod2","").replace("_cod3","").replace("_MA","")
					line = re.sub(r'\s+', ' ', line)
					print(line, sep=' ', end='', flush=True)
print(";")
f.close()

#DEFINE SET MA_cod2
print("\tcharset MA_cod2 =", sep=' ', end='', flush=True)
f = open(new, "r")
for line in f:
	line=line.replace('\t','')
	if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
	#print(line,end = ' ')
		if "_MA_cod2" in line:
			for word in genes:
				if word in line:
					#print(word)
					line=line.replace("\n","").replace(word,"").replace("=","").replace(";","").replace("charset","").replace("updated_","").replace("_cod1","").replace("_cod2","").replace("_cod3","").replace("_MA","")
					line = re.sub(r'\s+', ' ', line)
					print(line, sep=' ', end='', flush=True)
print(";")
f.close()

#DEFINE SET MA_cod3
print("\tcharset MA_cod3 =", sep=' ', end='', flush=True)
f = open(new, "r")
for line in f:
	line=line.replace('\t','')
	if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
	#print(line,end = ' ')
		if "_MA_cod3" in line:
			for word in genes:
				if word in line:
					#print(word)
					line=line.replace("\n","").replace(word,"").replace("=","").replace(";","").replace("charset","").replace("updated_","").replace("_cod1","").replace("_cod2","").replace("_cod3","").replace("_MA","")
					line = re.sub(r'\s+', ' ', line)
					print(line, sep=' ', end='', flush=True)
print(";")
f.close()

#DEFINE SET TM_cod1
print("\tcharset TM_cod1 =", sep=' ', end='', flush=True)
f = open(new, "r")
for line in f:
	line=line.replace('\t','')
	if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
	#print(line,end = ' ')
		if "_TM_cod1" in line:
			for word in genes:
				if word in line:
					#print(word)
					line=line.replace("\n","").replace(word,"").replace("=","").replace(";","").replace("charset","").replace("updated_","").replace("_cod1","").replace("_cod2","").replace("_cod3","").replace("_TM","")
					line = re.sub(r'\s+', ' ', line)
					print(line, sep=' ', end='', flush=True)
print(";")
f.close()

#DEFINE SET TM_cod2
print("\tcharset TM_cod2 =", sep=' ', end='', flush=True)
f = open(new, "r")
for line in f:
	line=line.replace('\t','')
	if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
	#print(line,end = ' ')
		if "_TM_cod2" in line:
			for word in genes:
				if word in line:
					#print(word)
					line=line.replace("\n","").replace(word,"").replace("=","").replace(";","").replace("charset","").replace("updated_","").replace("_cod1","").replace("_cod2","").replace("_cod3","").replace("_TM","")
					line = re.sub(r'\s+', ' ', line)
					print(line, sep=' ', end='', flush=True)
print(";")
f.close()

#DEFINE SET TM_cod3
print("\tcharset TM_cod3 =", sep=' ', end='', flush=True)
f = open(new, "r")
for line in f:
	line=line.replace('\t','')
	if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
	#print(line,end = ' ')
		if "_TM_cod3" in line:
			for word in genes:
				if word in line:
					#print(word)
					line=line.replace("\n","").replace(word,"").replace("=","").replace(";","").replace("charset","").replace("updated_","").replace("_cod1","").replace("_cod2","").replace("_cod3","").replace("_TM","")
					line = re.sub(r'\s+', ' ', line)
					print(line, sep=' ', end='', flush=True)
print(";")
f.close()

#DEFINE SET IM_cod1
print("\tcharset IM_cod1 =", sep=' ', end='', flush=True)
f = open(new, "r")
for line in f:
	line=line.replace('\t','')
	if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
	#print(line,end = ' ')
		if "_IM_cod1" in line:
			for word in genes:
				if word in line:
					#print(word)
					line=line.replace("\n","").replace(word,"").replace("=","").replace(";","").replace("charset","").replace("updated_","").replace("_cod1","").replace("_cod2","").replace("_cod3","").replace("_IM","")
					line = re.sub(r'\s+', ' ', line)
					print(line, sep=' ', end='', flush=True)
print(";")
f.close()

#DEFINE SET IM_cod2
print("\tcharset IM_cod2 =", sep=' ', end='', flush=True)
f = open(new, "r")
for line in f:
	line=line.replace('\t','')
	if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
	#print(line,end = ' ')
		if "_IM_cod2" in line:
			for word in genes:
				if word in line:
					#print(word)
					line=line.replace("\n","").replace(word,"").replace("=","").replace(";","").replace("charset","").replace("updated_","").replace("_cod1","").replace("_cod2","").replace("_cod3","").replace("_IM","")
					line = re.sub(r'\s+', ' ', line)
					print(line, sep=' ', end='', flush=True)
print(";")
f.close()

#DEFINE SET IM_cod3
print("\tcharset IM_cod3 =", sep=' ', end='', flush=True)
f = open(new, "r")
for line in f:
	line=line.replace('\t','')
	if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
	#print(line,end = ' ')
		if "_IM_cod3" in line:
			for word in genes:
				if word in line:
					#print(word)
					line=line.replace("\n","").replace(word,"").replace("=","").replace(";","").replace("charset","").replace("updated_","").replace("_cod1","").replace("_cod2","").replace("_cod3","").replace("_IM","")
					line = re.sub(r'\s+', ' ', line)
					print(line, sep=' ', end='', flush=True)
print(";")
f.close()
print('end;')
