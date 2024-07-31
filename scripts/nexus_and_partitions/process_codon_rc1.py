#!/usr/bin/env python

#TAKES AS INPUT FILE "new_charsets_codons_strand.nex"
#AND OUTPUTS A NEXUS PARTITION FILE AS 3 CODON PARTITIONS

import argparse

def process_nexus_file(input_file, output_file):
    cod1 = []
    cod2 = []
    cod3 = []

    with open(input_file, 'r') as infile:
        for line in infile:
            if 'charset' in line:
                if 'cod1' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    cod1.extend(processed_line.split())
                elif 'cod2' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    cod2.extend(processed_line.split())
                elif 'cod3' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    cod3.extend(processed_line.split())

    with open(output_file, 'w') as outfile:
        outfile.write("#nexus\n")
        outfile.write("begin sets;\n")
        outfile.write(f"\tcharset cod1 = {' '.join(cod1)};\n")
        outfile.write(f"\tcharset cod2 = {' '.join(cod2)};\n")
        outfile.write(f"\tcharset cod3 = {' '.join(cod3)};\n")
        outfile.write("end;\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a NEXUS file.')
    parser.add_argument('input_file', type=str, help='The input NEXUS file')
    parser.add_argument('output_file', type=str, help='The output NEXUS file')

    args = parser.parse_args()
    
    process_nexus_file(args.input_file, args.output_file)
