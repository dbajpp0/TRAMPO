from operator import itemgetter
import sys

script_name, gene_order, partition = sys.argv

# empty dictionary for the go structure. The goal is to fill it as follows:
'''
{'nd6': 'neg',
 'atp6': 'pos',
 'atp8': 'pos',
 'cob': 'pos',
 'cox1': 'pos',
 'cox2': 'pos',
 'cox3': 'pos',
 'nd1': 'pos',
 'nd2': 'pos',
 'nd3': 'pos',
 'nd4': 'pos',
 'nd5': 'pos',
 'ndl': 'pos'} '''
dict_go={}
with open(gene_order, 'r') as gene_order_file:
	for line in gene_order_file:
		# remove \n from the line
		lines = line.strip('\n')
		# pick the positive chain line
		if line.startswith('positive:'):
			# remove positive:
			line = line.replace('positive:','')
			# get the gene names
			genes = line.split(',')
			# adjust each gene name
			for gene in genes:
				gene = gene.replace('\n','')
				# put the gene name as key and the chain as value
				dict_go[gene]='pos'
		# pick the negative chain line
		if line.startswith('negative:'):
			# remove negative:
			line = line.replace('negative:','')
			# get the gene names
			genes = line.split(',')
			# adjust each gene name
			for gene in genes:
				gene = gene.replace('\n','')
				# put the gene name as key and the chain as value
				dict_go[gene]='neg'

# rearrange the dictionary sturcure and order (alphabetically)
sorted_data = sorted(dict_go.items(), key=lambda x: (x[1], x[0]))
dict_go = dict(sorted_data)
'''
{'nd6': 'neg',
 'atp6': 'pos',
 'atp8': 'pos',
 'cob': 'pos',
 'cox1': 'pos',
 'cox2': 'pos',
 'cox3': 'pos',
 'nd1': 'pos',
 'nd2': 'pos',
 'nd3': 'pos',
 'nd4': 'pos',
 'nd5': 'pos',
 'ndl': 'pos'} '''

# empty dictionary, useful to get final name and charset structures
new_partition_dict={}
# iterate over the go items
for gene, chain in dict_go.items():
	# open the partition file
	with open(partition, 'r') as partiontion_file:
		for line in partiontion_file:
			# take into account only charset lines
			if line.startswith('\t') :
				# e.g if 'nd2 in line'
				if gene in line:
					# remove the \n and \t, put it plain
					line = line.replace('\n','').replace('\t','')
					# get charset name and position separately
					charset_name, position= line.split('=')
					# minor name adjustment
					charset_name = charset_name.replace('charset ','')
					# get new charset name (e.g n2_TM_p1)
					new_charset_name = chain+charset_name.replace(gene,'')
					# if this name is not in the empty dictionary then fill with it for the first time
					if new_charset_name not in new_partition_dict:
						# charset name as key and position as value
						new_partition_dict[new_charset_name]=position.replace(' ;','')
					else:
						# if this charset name already exists hence append the new position to the previous one(s)
						new_partition_dict[new_charset_name]=[new_partition_dict[new_charset_name],position.replace(' ;','')]
					


# print everything on screen to save it			
print('#nexus')
print('begin sets;')
for k, v in new_partition_dict.items():
	# minor adjustment for the complete charset name
	v = str(v).replace('[','').replace(']','').replace("'",'').replace(',','')
	print('\tcharset '+k+'='+v+';')
print('end;')
