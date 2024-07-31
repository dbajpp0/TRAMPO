#!/usr/bin/env python

#TAKES AS INPUT FILE "new_charsets_codons_strand.nex"
#AND OUTPUTS A NEXUS PARTITION FILE AS
#6 PARTITIONS:
#CODON 1 SPLIT BY STRAND (neg_cod1, pos_cod1)
#CODON 3 SPLIT BY STRAND (neg_cod3, pos_cod3)
#CODON 2 SPLIT BY REGION (TM, NO) WHERE "NO" IS "MA"+"IM


import argparse

def process_nexus_file(input_file, output_file):

    neg_cod1 = []
    pos_cod1 = []
    neg_cod3 = []
    pos_cod3 = []
    NO_cod2  = []
    TM_cod2  = []

    with open(input_file, 'r') as infile:
        for line in infile:
            if 'charset' in line:
                if 'neg_' in line and '_cod1' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    neg_cod1.extend(processed_line.split())
                elif 'pos_' in line and '_cod1' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    pos_cod1.extend(processed_line.split())

                elif 'neg_' in line and '_cod3' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    neg_cod3.extend(processed_line.split())
                elif 'pos_' in line and '_cod3' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    pos_cod3.extend(processed_line.split())
                    
                elif '_cod2' in line and ('_MA_' in line or '_IM' in line):
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    NO_cod2.extend(processed_line.split())

                elif '_cod2' in line and '_TM_' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    TM_cod2.extend(processed_line.split())

    with open(output_file, 'w') as outfile:
        outfile.write("#nexus\n")
        outfile.write("begin sets;\n")
        outfile.write(f"\tcharset neg_cod1 = {' '.join(neg_cod1)};\n")
        outfile.write(f"\tcharset pos_cod1 = {' '.join(pos_cod1)};\n")
        outfile.write(f"\tcharset neg_cod3 = {' '.join(neg_cod3)};\n")
        outfile.write(f"\tcharset pos_cod3 = {' '.join(pos_cod3)};\n")
        outfile.write(f"\tcharset NO_cod2 = {' '.join(NO_cod2)};\n")
        outfile.write(f"\tcharset TM_cod2 = {' '.join(TM_cod2)};\n")
        outfile.write("end;\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a NEXUS file.')
    parser.add_argument('input_file', type=str, help='The input NEXUS file')
    parser.add_argument('output_file', type=str, help='The output NEXUS file')

    args = parser.parse_args()
    
    process_nexus_file(args.input_file, args.output_file)
