import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import sys
from statsmodels.stats.multitest import multipletests
from scipy import stats

pd.options.mode.chained_assignment = None
	
args = sys.argv[1:]
	
def perform_boxplot(data, title, colors):

	fig=px.box(data, x="Charset", y="GC_frequency", color='Charset', facet_col='CodonPosition', facet_col_wrap=1 , color_discrete_map=colors, template='simple_white')
	fig.update_traces(width=0.5)
	fig.update_layout(height=1000, width=1000)
	fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]+ " codon positions"))
	if title == "by chain":
		fig.update_xaxes(tickangle=0, title=None, ticks="outside", categoryorder='array', 
		             categoryarray=sorted(data['Charset'].unique(), 
		                                  key=lambda x: (x.split('_')[1], x.split('_')[0])))

# Statistical tests
	data['TEST'] = data['Charset'] + '_' + data['CodonPosition']
	group_codons = data['TEST'].unique()
	results=[]

	for i in range(len(group_codons)):
		for j in range(i+1, len(group_codons)):
			if group_codons[i].split('_')[1] == group_codons[j].split('_')[1]:

				group_codon_1 = group_codons[i]
				group_codon_2 = group_codons[j]

				data_1 = data[data['TEST'] == group_codon_1]['GC_frequency']
				data_2 = data[data['TEST'] == group_codon_2]['GC_frequency']

				stat, p_val = stats.mannwhitneyu(data_1, data_2)

				results.append({
						'Group_Domain_1': group_codon_1,
						'Group_Domain_2': group_codon_2,
						'MannWhitneyU_statistic': stat,
						'p_value': p_val
					})

	results_df = pd.DataFrame(results)
	corrected_p_vals = multipletests(results_df['p_value'], method='bonferroni')[1]
	results_df['corrected_p_value'] = corrected_p_vals

	mean_stdev = data.groupby('TEST').agg({'GC_frequency': ['mean', 'std']})
	mean_stdev.columns = ['mean_Freq', 'stdev_Freq']
	mean_stdev = mean_stdev.reset_index()
	
	modified_title=title.replace(' ','')

	results_df.to_csv(os.path.join(args[2], f'GC_frequency_{modified_title}_wilcoxon-test.tsv'), sep='\t', index=False)
	mean_stdev.to_csv(os.path.join(args[2], f'GC_frequency_{modified_title}_mean-stdev-test.tsv'), sep='\t', index=False)


	return fig
	
	
df_freq = pd.read_csv(args[0], sep='\t')
df_domains =  df_freq[df_freq['Charset'].isin(['IM', 'MA', 'TM'])].reset_index(drop=True)
df_domains =  df_domains[df_domains['CodonPosition'].isin(['First', 'Second', 'Third'])].reset_index(drop=True)
colors = {'IM': "#E69F00", 'MA': "#56B4E9", 'TM': "#009E73"}

fig_domains=perform_boxplot(df_domains, 'by domain', colors)

fig_domains.write_html(os.path.join(args[1],"GC_frequency_by_domain.html"))
fig_domains.write_image(os.path.join(args[1],"GC_frequency_by_domain.pdf"))

if args[3] != "1":
	df_chain = df_freq[df_freq['Charset'].isin(['pos_TM', 'pos_MA', 'pos_IM', 'neg_TM', 'neg_MA', 'neg_IM'])]
	df_chain =  df_chain[df_chain['CodonPosition'].isin(['First', 'Second', 'Third'])].reset_index(drop=True)
	colors = {'pos_TM':'#E8F086', 'pos_MA':'#6FDE6E', 
		 'pos_IM':'#235FA4', 'neg_TM':'#FF4242',
		 'neg_MA': '#A691AE', 'neg_IM':'#0A284B'}
	fig_chains = perform_boxplot(df_chain, 'by chain', colors)
	fig_chains.write_html(os.path.join(args[1],"GC_frequency_by_chain.html"))
	fig_chains.write_image(os.path.join(args[1],"GC_frequency_by_chain.pdf"))
