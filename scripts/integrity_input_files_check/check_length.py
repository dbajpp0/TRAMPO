from Bio import SeqIO
import sys
import statistics

script_name, file, basename = sys.argv

#check the outlier length of sequences
def check_length(file,basename):
	seq_length=[]
	for seqrecord in SeqIO.parse(file ,'fasta'):
		seq_length.append(len(seqrecord.seq))
	avg=statistics.mean(seq_length)
	stdev=statistics.stdev(seq_length)
	for seqrecord in SeqIO.parse(file ,'fasta'):
		if len(seqrecord.seq) > avg+(stdev*3) or len(seqrecord.seq) < avg-(stdev*3):
			print('Warning: the length of ' + str(seqrecord.id)+ ' in ' + 
			basename + ' differs more than three standard deviation. Check it carefully')

check_length(file,basename)
