from Bio import SeqIO
import sys

script_name, alignment_aa, nucleotide_seq, outputfile = sys.argv

def align_nt_to_aa(alignment,nucleotide_seq,outputfile):
	#aligns nt sequences by codon to the existing aa alignment
	with open(outputfile,'w') as nt_alignment:
		for al_sequence in SeqIO.parse(alignment,'fasta'):
			for nt_sequence in SeqIO.parse(nucleotide_seq, 'fasta'):
				if al_sequence.id == nt_sequence.id:
					seq='' #it is 'refilled' with adjacent codon
					c=0
					for x in al_sequence.seq:	
						if x != '-':
							x = 3*int(c+1)-3
							codon=nt_sequence.seq[x:x+3]
							seq=seq+str(codon)
							c+=1
						else:
							gap='---'
							seq=seq+gap		
					nt_alignment.write('>'+nt_sequence.id+'\n'+seq+'\n')
					break
					
align_nt_to_aa(alignment_aa, nucleotide_seq, outputfile)
