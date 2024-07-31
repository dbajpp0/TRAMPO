#!/usr/bin/env python

# TAKES AS INPUT FILE "new_charsets_codons_strand.nex"
# AND OUTPUTS A NEXUS PARTITION FILE AS 3 DOMAIN PARTITIONS

import argparse

def process_nexus_file(input_file):
	MA = []
	TM = []
	IM = []

	with open(input_file, 'r') as infile:
		for line in infile:
			line = line.replace("\3", "")  # Remove the string "\3" from each line
			if 'charset' in line:
				if 'MA_cod1' in line:
					processed_line = line.split('=')[1].replace(';', '').replace('\\3', '').strip()
					MA.extend(processed_line.split())
				elif 'TM_cod1' in line:
					processed_line = line.split('=')[1].replace(';', '').replace('\\3', '').strip()
					TM.extend(processed_line.split())
				elif 'IM_cod1' in line:
					processed_line = line.split('=')[1].replace(';', '').replace('\\3', '').strip()
					IM.extend(processed_line.split())

	print("#nexus")
	print("begin sets;")
	print(f"\tcharset MA = {' '.join(MA)};")
	print(f"\tcharset TM = {' '.join(TM)};")
	print(f"\tcharset IM = {' '.join(IM)};")
	print("end;")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="DESCRIPTION", formatter_class=argparse.RawTextHelpFormatter)
	requiredName = parser.add_argument_group('required named arguments')
	requiredName.add_argument("-a", "--file_new_charsets", required=True, 
						   help="Path to directory with fasta files")
						   

	args = parser.parse_args()
	
	process_nexus_file(args.file_new_charsets)

