import re
import sys
from Bio import SeqIO
import pandas as pd
import os

script_name, sequence, tables = sys.argv

# re-arrange the thmm tables' names
def transform_dataframe(df, gene):
	# put some fixed variables to parse the tmhmm tables
	GENE_COLUMN_NAME = 'Gene'
	START_COLUMN_NAME = 'Start'
	END_COLUMN_NAME = 'End'
	DOMAIN_COLUMN_NAME = 'Domain'
	COLUMNS_TO_DROP = ['Species', 'TMHMM', 'Range']
	# renames column names
	df[['Start', 'End']] = df['Range'].str.split(n=1, expand=True)
	df[DOMAIN_COLUMN_NAME] = df[DOMAIN_COLUMN_NAME].str.upper()
	df[DOMAIN_COLUMN_NAME] = df[DOMAIN_COLUMN_NAME].str.replace('TMHELIX', 'TM')
	df[DOMAIN_COLUMN_NAME] = df[DOMAIN_COLUMN_NAME].str.replace('INSIDE', 'MA')
	df[DOMAIN_COLUMN_NAME] = df[DOMAIN_COLUMN_NAME].str.replace('OUTSIDE', 'IM')
	df = df.drop(COLUMNS_TO_DROP, axis=1)
	df.insert(loc=0, column=GENE_COLUMN_NAME, value=gene)
	df = df[[GENE_COLUMN_NAME, START_COLUMN_NAME, END_COLUMN_NAME, DOMAIN_COLUMN_NAME]]
	return df
		
# dictionary of accepted names
names={	'ATP6': ['ATP6', 'A6','MT-ATP6', 'ATPASE6'] ,
	'ATP8': ['ATP8','A8', 'MT-ATP8', 'ATPASE8'] ,
	'COX1': ['COX1','MT-CO1', 'CO1',  'COXI', 'MTCO1', 'MTCOX1','MTCOXI'] ,	   
	'COX2': ['COX2','MT-CO2', 'CO2',  'COXII', 'MTCO2', 'MTCOX2','MTCOXII'] ,
	'COX3': ['COX3','MT-CO3', 'CO3',  'COXIII', 'MTCO3', 'MTCOX3','MTCOXIII'] ,
	'COB': ['COB','MT-CYB', 'CYTB', 'MTCYB'] ,
	'ND1': ['ND1', 'MT-ND1', 'MTND1', 'NADH1', 'NAD1'] ,
	'ND2': ['ND2', 'MT-ND2', 'MTND2', 'NADH2', 'NAD2' ] ,
	'ND3': ['ND3', 'MT-ND3', 'MTND3', 'NADH3', 'NAD3'] ,
	'ND4': ['ND4', 'MT-ND4', 'MTND4', 'NADH4', 'NAD4'] ,
	'NDL': ['NDL','MT-ND4L', 'MTND4L', 'NADH4L', 'ND4L', 'NADL', 'NAD4L', 'NADHL'] ,
	'ND5': ['ND5', 'MT-ND5', 'MTND5', 'NADH5', 'NAD5'] ,
	'ND6': ['ND6', 'MT-ND6', 'MTND6', 'NADH6', 'NAD6']
	}
         
## check the sequences
print('Analyzing optional files integrity...')
#possible nucleotide names
ambiguos_dna = ['A', 'C', 'G', 'T', 'R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'N']
#writes a new file (user.fas) with the info passed from the user
with open('templates/sequences/user.fas', 'w') as user_file:
	for seqrecord in SeqIO.parse(sequence, 'fasta'):
		counter = sum(seqrecord.seq.upper().count(aa) for aa in ambiguos_dna)
		if counter < len(seqrecord.seq):  # Sequences are composed of aminoacids
			for key, value in names.items():
				for v in value:
					if v in seqrecord.id.upper():
						if 'ND4' not in key:
							seqrecord.id = value[0].lower() + '_user'
						elif 'NDL' not in key:
							# To assess if it is nd4 or nl, search for the 'l'
							length = len(v)
							search = seqrecord.id.upper().find(v)
							if seqrecord.id[search + length].lower() == 'l':
								seqrecord.id = 'nl_user'
							else:
								seqrecord.id = 'nd4_user'
						seqrecord.description = ''
						SeqIO.write(seqrecord, user_file, 'fasta')
			
		else:
			raise Exception('You must pass an amino acid sequence as input, not a nucleotide one')
print('Optional sequence files correctly evaluated!')

## check the tables
print('Checking optional tables integrity...')
#create an emtpty df
all_tables = pd.DataFrame()

for file in os.listdir(tables):
	try:
		#check tables names
		gene = [key for key, value in names.items() for v in value if file[:file.rfind('.')].upper() == v][0].upper()
	except IndexError:
		raise Exception('TMpipe Error: Name of TMHMM table is incorrect. Check the manual to know how to rename them')
	
	df = pd.read_csv(os.path.join(tables, file), sep='\t', comment='#', names=['Species', 'TMHMM', 'Domain', 'Range', 'Start', 'End'])
	df = transform_dataframe(df, gene)
	all_tables = pd.concat([all_tables, df], ignore_index=True)

all_tables.to_csv('templates/model_organism_tables/user.tsv', index=False, sep='\t')

print('Optional tables correctly evaluated!')

