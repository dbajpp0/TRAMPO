import os
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
import sys

pd.options.mode.chained_assignment = None

args = sys.argv[1:]


def perform_RSCU_stats(data, title):
	data['TEST'] = data['Charset'] + '_' + data['Codon']
	group_domains = data['TEST'].unique()
	results = []
	for i in range(len(group_domains)):
		for j in range(i+1, len(group_domains)):
			if group_domains[i].split('_')[1] == group_domains[j].split('_')[1]:
				
				group_domain_1 = group_domains[i]
				group_domain_2 = group_domains[j]
				
				
				# Filter data for the two group domains
				data_1 = data[data['TEST'] == group_domain_1]['RSCU']
				data_2 = data[data['TEST'] == group_domain_2]['RSCU']
				
				# Perform Mann-Whitney U test
				stat, p_val = stats.mannwhitneyu(data_1, data_2)
				
				# Append results
				results.append({
					'Group_Domain_1': group_domain_1,
					'Group_Domain_2': group_domain_2,
					'MannWhitneyU_statistic': stat,
					'p_value': p_val
				})

	# Convert results to DataFrame
	results_df = pd.DataFrame(results)
	# Apply Bonferroni correction
	corrected_p_vals = multipletests(results_df['p_value'], method='bonferroni')[1]

	# Update corrected p-values in the results DataFrame
	results_df['corrected_p_value'] = corrected_p_vals
	mean_stdev = data.groupby('TEST').agg({'RSCU': ['mean', 'std']})
	mean_stdev.columns = ['mean_Freq', 'stdev_Freq']
	mean_stdev = mean_stdev.reset_index()
	
	modified_title=title.replace(' ','')
	
	results_df.to_csv(os.path.join(args[1], f'RSCU_{modified_title}_wilcoxon-test.tsv'), sep='\t', index=False)
	mean_stdev.to_csv(os.path.join(args[1], f'RSCU_{modified_title}_mean-stdev-test.tsv'), sep='\t', index=False)


df_RSCU = pd.read_csv(args[0], sep='\t')
df_domains = df_RSCU[df_RSCU['Charset'].isin(['IM', 'MA', 'TM'])]

perform_RSCU_stats(df_domains, 'by domain')

if args[2] != "1":
	df_chain = df_RSCU[df_RSCU['Charset'].isin(['pos_TM', 'pos_MA', 'pos_IM', 'neg_TM', 'neg_MA', 'neg_IM', 'Combined'])]
	perform_RSCU_stats(df_chain, 'by chain')

