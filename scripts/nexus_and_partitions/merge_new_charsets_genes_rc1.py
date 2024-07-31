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
genes = ["atp6","atp8","cob","cox1","cox2","cox3","nd1","nd2","nd3","nd4","nd5","nd6","ndl"]

# Create a dictionary to store lines associated with names
name_lines = {name: [] for name in genes}

# Open the file for reading
with open(new, 'r') as file:
	for line in file:
		if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
			line = line.replace('\t','').strip()  # Remove leading and trailing whitespace
		
		# Check if any name is in the current line
		for name in genes:
			if name in line:
				line=line.replace(name,"").replace("\n","").replace("=","").replace(";","").replace("charset","").replace("updated_","").replace("_MA","").replace("_TM","").replace("_IM","")  #strip features of nexus charsets
				name_lines[name].append(line)  # Store the line associated with the name

# Print the lines associated with each name
for name, lines in name_lines.items():
	if lines:
		print("\tcharset ",f"{name}"," = ",sep='', end='', flush=True)
		for line in lines:
			line = re.sub(r'\s+', ' ', line) # Repalce multiples spaces for a single one
			print(line,  sep='', end='')
		print(";")
print('end;')
