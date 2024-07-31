#!/usr/bin/env python

#TAKES AS INPUT FILE "new_charsets_codons_strand.nex"
#AND OUTPUTS A NEXUS PARTITION FILE AS
#12 PARTITIONS: BY STRAND (2) AND BY CODON (3)
#AND BY 2 REGIONS (TM, NO) SINCE MA AND IM BLOCKS
#ARE MERGED IN A SINGLE ONE CALLED "NO"


import argparse

def process_nexus_file(input_file, output_file):

    neg_TM_cod1 = []
    neg_TM_cod2 = []
    neg_TM_cod3 = []
    pos_TM_cod1 = []
    pos_TM_cod2 = []
    pos_TM_cod3 = []
    neg_NO_cod1 = []
    neg_NO_cod2 = []
    neg_NO_cod3 = []
    pos_NO_cod1 = []
    pos_NO_cod2 = []
    pos_NO_cod3 = []

    with open(input_file, 'r') as infile:
        for line in infile:
            if 'charset' in line:
                if 'neg_' in line and '_TM_' in line and '_cod1' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    neg_TM_cod1.extend(processed_line.split())
                if 'neg_' in line and '_TM_' in line and '_cod2' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    neg_TM_cod2.extend(processed_line.split())
                if 'neg_' in line and '_TM_' in line and '_cod3' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    neg_TM_cod3.extend(processed_line.split())

                if 'pos_' in line and '_TM_' in line and '_cod1' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    pos_TM_cod1.extend(processed_line.split())
                if 'pos_' in line and '_TM_' in line and '_cod2' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    pos_TM_cod2.extend(processed_line.split())
                if 'pos_' in line and '_TM_' in line and '_cod3' in line:
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    pos_TM_cod3.extend(processed_line.split())
                    
                if 'neg_' in line and '_cod1' in line and ('_MA_' in line or '_IM' in line):
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    neg_NO_cod1.extend(processed_line.split())
                if 'neg_' in line and '_cod2' in line and ('_MA_' in line or '_IM' in line):
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    neg_NO_cod2.extend(processed_line.split())
                if 'neg_' in line and '_cod3' in line and ('_MA_' in line or '_IM' in line):
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    neg_NO_cod3.extend(processed_line.split())
                    
                if 'pos_' in line and '_cod1' in line and ('_MA_' in line or '_IM' in line):
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    pos_NO_cod1.extend(processed_line.split())
                if 'pos_' in line and '_cod2' in line and ('_MA_' in line or '_IM' in line):
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    pos_NO_cod2.extend(processed_line.split())
                if 'pos_' in line and '_cod3' in line and ('_MA_' in line or '_IM' in line):
                    processed_line = line.split('=')[1].replace(';', '').strip()
                    pos_NO_cod3.extend(processed_line.split())

    with open(output_file, 'w') as outfile:
        outfile.write("#nexus\n")
        outfile.write("begin sets;\n")
        outfile.write(f"\tcharset neg_TM_cod1 = {' '.join(neg_TM_cod1)};\n")
        outfile.write(f"\tcharset neg_TM_cod2 = {' '.join(neg_TM_cod2)};\n")
        outfile.write(f"\tcharset neg_TM_cod3 = {' '.join(neg_TM_cod3)};\n")
        outfile.write(f"\tcharset pos_TM_cod1 = {' '.join(pos_TM_cod1)};\n")
        outfile.write(f"\tcharset pos_TM_cod2 = {' '.join(pos_TM_cod2)};\n")
        outfile.write(f"\tcharset pos_TM_cod3 = {' '.join(pos_TM_cod3)};\n")
        outfile.write(f"\tcharset neg_NO_cod1 = {' '.join(neg_NO_cod1)};\n")
        outfile.write(f"\tcharset neg_NO_cod2 = {' '.join(neg_NO_cod2)};\n")
        outfile.write(f"\tcharset neg_NO_cod3 = {' '.join(neg_NO_cod3)};\n")
        outfile.write(f"\tcharset pos_NO_cod1 = {' '.join(pos_NO_cod1)};\n")
        outfile.write(f"\tcharset pos_NO_cod2 = {' '.join(pos_NO_cod2)};\n")
        outfile.write(f"\tcharset pos_NO_cod3 = {' '.join(pos_NO_cod3)};\n")
        outfile.write("end;\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a NEXUS file.')
    parser.add_argument('input_file', type=str, help='The input NEXUS file')
    parser.add_argument('output_file', type=str, help='The output NEXUS file')

    args = parser.parse_args()
    
    process_nexus_file(args.input_file, args.output_file)
