import pandas as pd
from Bio import SeqIO, AlignIO
import os
import sys
from Bio.Nexus import Nexus

script_name, alignment, table, organism = sys.argv
out_nexus_aa = alignment.replace('.fas','.nex').replace('Alignment','03_Nexus')
out_nexus_nt = out_nexus_aa.replace('aa', 'nt').replace('Alignment','03_Nexus')

def create_partitions(table,domain,molecule):
	# subset the table depending on domain name (the table passed must be a subsetted one from the model organism table. drop the index!
	dataframe=table[table['Domain'] == domain].reset_index(drop=True)
	# make a dictionary using starts and ends
	start_end_dict=dataframe.set_index('Start').to_dict()['End']
	string=domain+' ='
	# what to trim will be filled with minimum and maximum starts and ends
	what_to_trim=[]
	for start,end in start_end_dict.items():
		if molecule == 'protein':
			string=string+' '+str(start)+'-'+str(end)
			what_to_trim.extend([start,end])
		else:
			string=string+' '+str((3*start)-2)+'-'+str(3*end)
			what_to_trim.extend([(3*start)-2,3*end])
	trimstart=min(what_to_trim)
	trimend=max(what_to_trim)
	string=string+';'
	# returns the string that must be written in nexus file and the start and end to be trimmed
	return string, trimstart, trimend

def move_domains_and_save_nexus(alignment, table, out_nexus_aa, out_nexus_nt, organism):
# pick up the gene name, it will be necessary to subset the table
	gene_name = os.path.basename(alignment).split('_')[0].upper()
	# read the model organism table as a dataframe
	df=pd.read_csv(table, sep='\t')
	# subset the table depending on gene name
	subsetted_table = df[df['Gene'] == gene_name]
	# create output files : nexus nt and aa
	with open(out_nexus_aa, 'a') as nexus_file_aa:
		with open(out_nexus_nt,'a') as nexus_file_nt:
			# parse the fasta sequences until arrive to the gene of interest (it's the model organism one - eg atp8_hsa)
			for sequence in SeqIO.parse(alignment, 'fasta'):
				if organism in sequence.id:
					for index,row in subsetted_table.iterrows():
						# pick up the domain name, start and end of each domain from the model organism table (remeber, it's reduced to the gene of interest)
						start=int(row['Start'])
						end=int(row['End'])
						domain=row['Domain']
						# slice the sequence depending on the start and end
						seq_slide=sequence.seq[start-1:end]
						# count the gaps
						gaps=seq_slide.count('-')
						# if gaps are present then shift the whole portions and creates the final table
						if gaps > 0:
							df.at[index,'Start']+=gaps
							df.at[index,'End']+=gaps

					#each obj created here will contain three variables: the string to be written in the nexus file, the start and end to be trimmed.
					MA_AA=create_partitions(subsetted_table,'MA','protein')
					TM_AA=create_partitions(subsetted_table,'TM','protein')
					IM_AA=create_partitions(subsetted_table,'IM','protein')

					MA_NT=create_partitions(subsetted_table,'MA','dna')
					TM_NT=create_partitions(subsetted_table,'TM','dna')
					IM_NT=create_partitions(subsetted_table,'IM','dna')
					
					# group trim starts and ends
					trimstart_aa=[MA_AA[1],TM_AA[1],IM_AA[1]]
					trimstart_aa=min(trimstart_aa)
					trimend_aa=[MA_AA[2],TM_AA[2],IM_AA[2]]
					trimend_aa=max(trimend_aa)

					trimstart_nt=[MA_NT[1],TM_NT[1],IM_NT[1]]
					trimstart_nt=min(trimstart_nt)
					trimend_nt=[MA_NT[2],TM_NT[2],IM_NT[2]]
					trimend_nt=max(trimend_nt)
					

					#write the partitions files
					nexus_file_aa.write('begin sets;\n'+
										'\tcharset '+ MA_AA[0]+'\n'+
										'\tcharset '+ TM_AA[0]+'\n'+
										'\tcharset '+ IM_AA[0]+'\n'+
										'end;')

					nexus_file_nt.write('begin sets;\n'+
										'\tcharset '+ MA_NT[0]+'\n'+
										'\tcharset '+ TM_NT[0]+'\n'+
										'\tcharset '+ IM_NT[0]+'\n'+
										'end;')
					break

			else:
				if organism != 'cel':
					raise Exception('No association with gene name found. Please consider to rename your file as described in the manual')
	return trimstart_aa, trimend_aa, trimstart_nt, trimend_nt


def remove_gaps_and_modelorganism(nexfile, trimstart, trimend, taxon_to_exclude):
	# Read the alignment
	align = AlignIO.read(nexfile, 'nexus')
	length = align.get_alignment_length()

	# Get gap positions
	nexus = Nexus.Nexus(nexfile)
	gaps = nexus.gaponly()
	gaps.extend(range(1, int(trimstart)))
	gaps.extend(range(trimend, length + 1))

	# Print information about removed characters
	if '_aa_aligned' in nexfile:
		print('The original alignment of ' + os.path.basename(nexfile) + ' lost ' + str(len(gaps)) + '/' + str(length) + ' - ' +
			  str(round(100 * len(gaps) / length, 2)) + ('% of amino acid characters'))
	else:
		print('The original alignment of ' + os.path.basename(nexfile) + ' lost ' + str(len(gaps)) + '/' + str(length) + ' - ' +
			  str(round(100 * len(gaps) / length, 2)) + ('% of nucleotide characters'))

	try:
		# Write Nexus data excluding gaps and specified taxon
		nexus.write_nexus_data(nexfile, exclude=gaps, delete=[taxon_to_exclude])
	except Exception:
		# Write Nexus data excluding gaps only if taxon_to_exclude is not present
		nexus.write_nexus_data(nexfile, exclude=gaps)

	return nexfile

	
trimstart_aa, trimend_aa, trimstart_nt, trimend_nt = move_domains_and_save_nexus(alignment, table, out_nexus_aa, out_nexus_nt,organism)
remove_gaps_and_modelorganism(out_nexus_aa, trimstart_aa, trimend_aa, organism)
remove_gaps_and_modelorganism(out_nexus_nt, trimstart_nt, trimend_nt, organism)

	

