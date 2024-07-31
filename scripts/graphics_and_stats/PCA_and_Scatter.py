#import seaborn as sns
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
from matplotlib import pyplot as plt
import sys
import os
import plotly.express as px
import plotly.io as pio


script_name, df, graphics_folder, gene_order = sys.argv

def scatter_plot(data, title, colors):
	data['dummy_size'] = 1
	
	fig = px.scatter(data, x='ATskew', y='GCskew', color='Charset', symbol='Position', opacity=0.7,
                    symbol_sequence=["circle", 'triangle-up', 'x'], color_discrete_map=colors, size='dummy_size', size_max=15)

# Customize the legend
	fig.update_layout(legend=dict(x=1.02, y=1, bordercolor='white', borderwidth=1, font=dict(size=20)),
                  title='AT-GC skews ' + title, template='plotly_white', autosize=False, width = 2000, height = 1000,
                   	xaxis=dict(tickfont=dict(size=30)), 
        		yaxis=dict(tickfont=dict(size=30)))

	return fig

def pca(data, title, colors):
	features=['ATskew','GCskew']
	x = data.loc[:, features].values
	y = data.loc[:,['Charset']].values
	x = StandardScaler().fit_transform(x)
	pca = PCA(n_components=2)
	principalComponents = pca.fit_transform(x)
	per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
	principalDf = pd.DataFrame(data = principalComponents, columns = ['PCA1', 'PCA2'])
	finalDf = pd.concat([principalDf, data[['Charset','Position']]], axis = 1)
	finalDf['dummy_size'] = 1
	
	fig = px.scatter(finalDf, x='PCA1', y='PCA2', color='Charset', symbol='Position', opacity=0.7,
                    symbol_sequence=["circle", 'triangle-up', 'x'], color_discrete_map=colors, size='dummy_size', size_max=15)

# Customize the legend
	fig.update_layout(legend=dict(x=1.02, y=1, bordercolor='white', borderwidth=1, font=dict(size=20)),
                  title='AT-GC skews ' + title, template='plotly_white', autosize=False, width = 2000, height = 1000 )

# Customize axis labels
	fig.update_xaxes(title='PC1 - {0}%'.format(per_var[0]), title_font=dict(size=15))
	fig.update_yaxes(title='PC2 - {0}%'.format(per_var[1]), title_font=dict(size=15))

	return fig


df_skews = pd.read_csv(df, sep='\t')
df_skews = df_skews[df_skews['Position'] != 'All']
df_domains = df_skews[df_skews['Charset'].isin(['IM', 'MA', 'TM'])].reset_index(drop=True)
colors = {'IM': "#E69F00", 'MA': "#56B4E9", 'TM': "#009E73"}

fig_domains = pca(df_domains, 'by Domains',colors)
fig_domains.write_html(os.path.join(graphics_folder , 'Skew-PCA_by_domain.html'))
fig_domains.write_image(os.path.join(graphics_folder , 'Skew-PCA_by_domain.pdf'))

scatter_domains = scatter_plot(df_domains, 'by Domains',colors)
scatter_domains.write_html(os.path.join(graphics_folder , 'Skew-scatter-plot_by_domain.html'))
scatter_domains.write_image(os.path.join(graphics_folder , 'Skew-scatter-plot_domain.pdf'))


if gene_order != "1":
	df_chain = df_skews[df_skews['Charset'].isin(['pos_TM', 'pos_MA', 'pos_IM', 'neg_TM', 'neg_MA', 'neg_IM'])].reset_index(drop=True)

	colors = {'pos_TM':'#E8F086', 'pos_MA':'#6FDE6E', 
		 'pos_IM':'#235FA4', 'neg_TM':'#FF4242',
		 'neg_MA': '#A691AE', 'neg_IM':'#0A284B'}
		 
	fig_chains = pca(df_chain, "by Chains", colors)
	fig_chains.write_html(os.path.join(graphics_folder , 'Skew-PCA_by_chain.html',))
	fig_chains.write_image(os.path.join(graphics_folder , 'Skew-PCA_by_chain.pdf'))
	
	scatter_chain = scatter_plot(df_chain, 'by Chains',colors)
	scatter_chain.write_html(os.path.join(graphics_folder , 'Skew-scatter-plot_by_chain.html'))
	scatter_chain.write_image(os.path.join(graphics_folder , 'Skew-scatter-plot_chain.pdf'))
