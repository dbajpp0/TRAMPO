#!/usr/bin/env python

import re
import os
import argparse

parser = argparse.ArgumentParser(description="DESCRIPTION", formatter_class=argparse.RawTextHelpFormatter)

requiredName = parser.add_argument_group('required named arguments')

requiredName.add_argument("-a", "--file_charsets", required=True, 
						  help="Path to directory with fasta files")

args = parser.parse_args()

## 3-Rename input parameters
char = args.file_charsets

f = open(char, "r")
print('#nexus')
print('begin sets;')

for line in f:
	if '#nexus' not in line and 'begin sets;' not in line and 'end;' not in line:
		input_string = line.replace('\t','')
		nom, _ = input_string.strip().split("=")
		nom = re.sub(r' +', ' ', nom).replace("charset ", "").replace(" ", "")

		pattern = r'(\w+)-(\w+)'
		key_value_pairs = re.findall(pattern, input_string)
		my_dict = dict(key_value_pairs)

		first_key = list(my_dict.keys())[0]
		first_value = list(my_dict.values())[0]

		# Set cod1 charset
		print("\tcharset ", nom, "_cod1 = ", sep='', end='', flush=True)
		for i in range(0, len(my_dict)):
			key = list(my_dict.keys())[i]
			value = list(my_dict.values())[i]
			print(f"{key}-{value}\\3", sep='', end=' ', flush=True)
		print(";")

		# Set cod2 charset
		print("\tcharset ", nom, "_cod2 = ", sep='', end='', flush=True)
		for i in range(0, len(my_dict)):
			key2 = int(list(my_dict.keys())[i]) + 1
			value = list(my_dict.values())[i]
			print(f"{key2}-{value}\\3", sep='', end=' ', flush=True)
		print(";")

		# Set cod3 charset
		print("\tcharset ", nom, "_cod3 = ", sep='', end='', flush=True)
		for i in range(0, len(my_dict)):
			key3 = int(list(my_dict.keys())[i]) + 2
			value = list(my_dict.values())[i]
			print(f"{key3}-{value}\\3", sep='', end=' ', flush=True)
		print(";")
print('end;')
