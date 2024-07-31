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


print('#nexus')
print('begin sets;')
### Define lists


f = open(new, "r")


# List of names to search for in the file
genes = ["atp6_cod1","atp8_cod1","cob_cod1","cox1_cod1","cox2_cod1","cox3_cod1","nd1_cod1","nd2_cod1","nd3_cod1","nd4_cod1","nd5_cod1","nd6_cod1","ndl_cod1","atp6_cod2","atp8_cod2","cob_cod2","cox1_cod2","cox2_cod2","cox3_cod2","nd1_cod2","nd2_cod2","nd3_cod2","nd4_cod2","nd5_cod2","nd6_cod2","ndl_cod2","atp6_cod3","atp8_cod3","cob_cod3","cox1_cod3","cox2_cod3","cox3_cod3","nd1_cod3","nd2_cod3","nd3_cod3","nd4_cod3","nd5_cod3","nd6_cod3","ndl_cod3"]

# Create a dictionary to store lines associated with names
name_lines = {name: [] for name in genes}

# Open the file for reading
for line in f:
	line=line.replace('\t','')
	if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
		line = line.strip()  # Remove leading and trailing whitespace
		line = line.replace("_MA","").replace("_TM","").replace("_IM","")
#		print(line)

		# Check if any name is in the current line
		for name in genes:
			if name in line:
				line=line.replace(name,"").replace("\n","").replace("=","").replace(";","").replace("charset","").replace("updated_","").replace("_MA","").replace("_TM","").replace("_IM","")  #strip features of nexus charsets
				name_lines[name].append(line)  # Store the line associated with the name

# Print the lines associated with each name
for name, lines in name_lines.items():
	if lines:
		print("charset ",f"{name}", " = ", sep='', end='', flush=True)
		for line in lines:
			line = re.sub(r'\s+', ' ', line) # Repalce multiples spaces for a single one
			print(line,  sep='', end='')
		print(";","\n")
f.close()
print('end;')

