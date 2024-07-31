from Bio import SeqIO
import pandas as pd
import os
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.Seq import Seq
import sys
from CAI import RSCU
from collections import Counter
from Bio.SeqUtils import GC123

script_name, folder, output_RSCU, output_AA, output_1_SKEW, output_23_SKEW, code = sys.argv

code = int(code)

accepted_file = ['nt_combined_regions_IM', 'nt_combined_regions_MA', 'nt_combined_regions_TM', 'nt_combined_regions.nex', 
			'nt_combined_strand_regions_neg_IM', 'nt_combined_strand_regions_neg_MA', 'nt_combined_strand_regions_neg_TM', 
			'nt_combined_strand_regions_pos_IM', 'nt_combined_strand_regions_pos_MA', 'nt_combined_strand_regions_pos_TM']

# formula to calculate the 2,3 skews
def ATCG_skew(seq,n1,n2):
	ag = seq.upper().count(n1) 
	tc = seq.upper().count(n2)
	try:
		skew = ag / float(ag + tc)
	except ZeroDivisionError:
		skew = 0.0
	return round(skew,4)

# four empty dataframe to be filled progressively
df_AA = pd.DataFrame()
df_RSCU = pd.DataFrame()
df_1_SKEW=pd.DataFrame()
df_23_SKEW=pd.DataFrame()

# iterate over each file
for partition in os.listdir(folder):
	if partition in accepted_file:
		# create the perfect charset name
		if 'nex' in partition:
			charset='Combined'
		else:
			charset=partition.replace('nt_combined_genes_regions_','').replace('nt_combined_strand_regions_','').replace('nt_combined_regions_','')
		# iterate over each sequence for each file
		for record in SeqIO.parse(os.path.join(folder, partition), 'nexus'):
			## aa frequency
			# translate the sequence depending on the genetic code
			translated = record.seq.translate(code)
			# get aminoacid frquency
			aminoacid_count=Counter(translated)
			del aminoacid_count['-']
			# put these values in a tmp dataframe
			tmp_df_aa = pd.DataFrame(aminoacid_count.items(), columns=['AA', 'Count'])
			# add two fixed columns to the tmp dataframes = species name and charset name
			tmp_df_aa['Species']=record.id
			tmp_df_aa['Charset']=charset
			# fill the real datframe with the tmp one
			df_AA = pd.concat([df_AA, tmp_df_aa], ignore_index=True)

			## codon usage
			# empty string, it will be filled with codons
			whole = str('')
			# emtpy dictionary, it will be filled with codon + species name
			d = {}
			# split the sequence per codon and put them in a list named codons
			codons = [record.seq[i:i+3] for i in range(0, len(record.seq), 3)]
			# iterate over the items of this list
			for codon in codons:
				# fill the whole with codon value
				whole += codon
				# append codon value + species name to the dictionary
				d[str(codon).upper()]=record.id
			# create empty list
			seqlist=[]
			# and append codons
			seqlist.append(whole)
			# calulate effective RSCU per species, it will be returned a dictionary
			rscu_dict = RSCU(seqlist, code)
			# create empty dictionary
			aa_rscu_df={}
			# iterate over the RSCU created dictionary
			for codon, rscu in rscu_dict.items():
				# and add the codon value as key and codon seq + rscu value to the empty dictionary 
				aa_rscu_df[codon]=[str(Seq(codon).translate(table=code)),rscu]
			# put everything in a tmp df
			temp_df_RSCU = pd.DataFrame([([k] + v) for k, v in aa_rscu_df.items()], columns=['Codon', 'AA','RSCU'])
			# add species name and charset name in the tmp dictionary
			temp_df_RSCU['Species']=record.id
			temp_df_RSCU['Charset']=charset
			# merge the tmp with the real df
			df_RSCU = pd.concat([df_RSCU, temp_df_RSCU], ignore_index=True)
			
			## GC CONTENT (know as the first skew)
			# get the GC skew for the whole seq
			try:
				GC = GC123(record.seq)
			except ZeroDivisionError:
				print('Warning: unable to calculate the first skew for ' + record.id + ' ' +  charset + '. Check the ' + partition + ' file for further details')
				GC = (0,0,0,0)
			# replace efficently result within a new dictionary
			d={}
			d['All']=round(GC[0],4)
			d['First']=round(GC[1],4)
			d['Second']=round(GC[2],4)
			d['Third']=round(GC[3],4)
			# get the AT%
			for k,v in d.items():
				AT = 100-v
				d[k]=[v,AT]
			# write everything in a tmp df
			temp_df_first = pd.DataFrame([([k] + v) for k, v in d.items()], columns=['CodonPosition','GC_frequency','AT_frequency'])
			temp_df_first['Species'] = record.id
			temp_df_first['Charset']= charset
			# bring the tml df in the real one
			df_1_SKEW = pd.concat([df_1_SKEW, temp_df_first], ignore_index=True)
			
			
			## SECOND THRIRD BIAS
			# calcualte at/gc skew over the entire sequence - does not counts for codon position
			tot = [[record.id, charset, 'All',ATCG_skew(record.seq,'G','C'), ATCG_skew(record.seq,'A','T')]]
			# empty sequences: one for each codon position
			first_pos=Seq('')
			second_pos=Seq('')
			third_pos=Seq('')
			# iterate over codons, obj built before in the RSCU section, to pick up the 1st, 2nd and 3rd position of each triplet
			for codon in codons:
				first_pos = first_pos + codon[0]
				second_pos = second_pos + codon[1]
				third_pos = third_pos + codon[2]

			# calcualte at/gc skew for each position
			first = [[record.id, charset, 'First',ATCG_skew(first_pos,'G','C'), ATCG_skew(first_pos,'A','T')]]
			second = [[record.id, charset, 'Second',ATCG_skew(second_pos,'G','C'), ATCG_skew(second_pos,'A','T')]]
			third = [[record.id, charset, 'Third',ATCG_skew(third_pos,'G','C'), ATCG_skew(third_pos,'A','T')]]
			
			# put everythin in a tmp df
			temp_df_23 = pd.DataFrame(tot, columns = ['Species','Charset','Position','GCskew','ATskew'])
			df_23_SKEW = pd.concat([df_23_SKEW, temp_df_23], ignore_index=True)
			temp_df_23 = pd.DataFrame(first, columns = ['Species','Charset','Position','GCskew','ATskew'])
			df_23_SKEW = pd.concat([df_23_SKEW, temp_df_23], ignore_index=True)
			temp_df_23 = pd.DataFrame(second, columns = ['Species','Charset','Position','GCskew','ATskew'])
			df_23_SKEW = pd.concat([df_23_SKEW, temp_df_23], ignore_index=True)
			temp_df_23 = pd.DataFrame(third, columns = ['Species','Charset','Position','GCskew','ATskew'])
			df_23_SKEW = pd.concat([df_23_SKEW, temp_df_23], ignore_index=True)
					
					
				
		
		
		
		
# write every real df in two distinct file
df_AA=df_AA[['Species','Charset', 'AA', 'Count']]
df_RSCU=df_RSCU[['Species','Charset', 'Codon', 'AA','RSCU']]
df_1_SKEW=df_1_SKEW[['Species','Charset', 'CodonPosition', 'GC_frequency','AT_frequency']]
df_AA.to_csv(output_AA, index=False, sep='\t')
df_RSCU.to_csv(output_RSCU, index=False, sep='\t')
df_1_SKEW.to_csv(output_1_SKEW, index=False, sep='\t')
df_23_SKEW.to_csv(output_23_SKEW, index=False, sep='\t')
