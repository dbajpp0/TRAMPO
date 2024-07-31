import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multitest import multipletests
import plotly.express as px
import sys

args = sys.argv[1:]

def perform_hist(data, title):
# Define the amino acid groups
	aa_groups = {'A': 'G1', 'G': 'G1', 'P': 'G1', 'S': 'G1', 'T': 'G1',
					'D': 'G2', 'E': 'G2', 'N': 'G2', 'Q': 'G2',
					'H': 'G3', 'K': 'G3', 'R': 'G3',
					'I': 'G4', 'L': 'G4', 'M': 'G4', 'V': 'G4',
					'F': 'G5', 'W': 'G5', 'Y': 'G5',
					'C': 'G6'}
	aa_groups_df = pd.DataFrame(aa_groups.items(), columns=['AA', 'Groups'])
	new_data = data.merge(aa_groups_df, on='AA', how='left')
	new_data['Groups_by_Domain'] = new_data['Charset'] + '_' + new_data['Groups']
	new_data.dropna(subset=['Groups'], inplace=True)
	group_domains = new_data['Groups_by_Domain'].unique()
	
	group_counts = new_data.groupby(['Charset', 'Groups'])['Count'].sum().unstack(fill_value=0)
	group_percentages = group_counts.div(group_counts.sum(axis=1), axis=0) * 100

	final_result = group_percentages.stack().reset_index()
	final_result.columns = ['Charset', 'Group', 'Percentage']
	
	counts = []

	
	results = []
	for i in range(len(group_domains)):
		for j in range(i+1, len(group_domains)):
			if title == 'by domain':
				if group_domains[i].split('_')[1] == group_domains[j].split('_')[1] and group_domains[i].split('_')[1] in aa_groups.values() and group_domains[j].split('_')[1] in aa_groups.values(): 
					group_domain_1 = group_domains[i]
					group_domain_2 = group_domains[j]
					
					# Filter data for the two group domains
					data_1 = new_data[new_data['Groups_by_Domain'] == group_domain_1]['Count']
					data_2 = new_data[new_data['Groups_by_Domain'] == group_domain_2]['Count']
					
					# Perform Mann-Whitney U test
					stat, p_val = stats.mannwhitneyu(data_1, data_2)
					
					# Append results
					results.append({
						'Group_Domain_1': group_domain_1,
						'Group_Domain_2': group_domain_2,
						'MannWhitneyU_statistic': stat,
						'p_value': p_val
					})
			else:
				if group_domains[i].split('_')[2] == group_domains[j].split('_')[2] and group_domains[i].split('_')[2] in aa_groups.values() and group_domains[j].split('_')[2] in aa_groups.values():
					group_domain_1 = group_domains[i]
					group_domain_2 = group_domains[j]
					
					# Filter data for the two group domains
					data_1 = new_data[new_data['Groups_by_Domain'] == group_domain_1]['Count']
					data_2 = new_data[new_data['Groups_by_Domain'] == group_domain_2]['Count']
					
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


	# Calculate mean and standard deviation
	mean_stdev = new_data.groupby('Groups_by_Domain').agg({'Count': ['mean', 'std']})
	mean_stdev.columns = ['mean_Freq', 'stdev_Freq']
	mean_stdev = mean_stdev.reset_index()
	
	modified_title=title.replace(' ','')

	results_df.to_csv(os.path.join(args[2], f'AminoAcid_frequency_{modified_title}_wilcoxon-test.tsv'), sep='\t', index=False)
	mean_stdev.to_csv(os.path.join(args[2], f'AminoAcid_frequency_{modified_title}_mean-stdev-test.tsv'), sep='\t', index=False)
	

	fig = px.histogram(final_result, x="Charset", y="Percentage", color="Group")
	if title == 'by chain':
		fig.update_xaxes(tickangle=0, title=None, ticks="outside", categoryorder='array')
	else:
		fig.update_xaxes(tickangle=0, title=None, ticks="outside", categoryorder='array')
	fig.update_yaxes(title="Relative Frequencies (%)")
	fig.update_traces(textposition='outside')
	fig.update_layout(
		{'plot_bgcolor': '#ffffff', 'paper_bgcolor': '#ffffff'},
		uniformtext_minsize=8, uniformtext_mode='show',
		autosize=False, width=2000, height=1000,
		title={'text': 'Amino acid frequency ' + title})

	# Show plot
	return fig
	
	
df_freq = pd.read_csv(args[0], sep='\t')
df_domains = df_freq[df_freq['Charset'].isin(['IM', 'MA', 'TM'])]
fig_domains=perform_hist(df_domains, 'by domain')

fig_domains.write_html(os.path.join(args[1],"AminoAcid_frequency_by_domain.html"))
fig_domains.write_image(os.path.join(args[1],"AminoAcid_frequency_by_domain.pdf"))

if args[3] != "1":
	df_chain = df_freq[df_freq['Charset'].isin(['pos_TM', 'pos_MA', 'pos_IM', 'neg_TM', 'neg_MA', 'neg_IM'])]
	fig_chains = perform_hist(df_chain, 'by chain')
	fig_chains.write_html(os.path.join(args[1],"AminoAcid_frequency_by_chain.html"))
	fig_chains.write_image(os.path.join(args[1],"AminoAcid_frequency_by_chain.pdf"))

