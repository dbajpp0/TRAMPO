import sys
import os

script_name, organism, file = sys.argv


# dictionary of accepted names
names={	'ATP6': ['ATP6', 'A6','MT-ATP6', 'ATPASE6'] ,
	'ATP8': ['ATP8','A8', 'MT-ATP8', 'ATPASE8'] ,
	'COX1': ['COX1','MT-CO1', 'CO1',  'COXI', 'MTCO1', 'MTCOX1','MTCOXI'] ,	   
	'COX2': ['COX2','MT-CO2', 'CO2',  'COXII', 'MTCO2', 'MTCOX2','MTCOXII'] ,
	'COX3': ['COX3','MT-CO3', 'CO3',  'COXIII', 'MTCO3', 'MTCOX3','MTCOXIII'] ,
	'COB': ['COB','MT-CYB', 'CYTB', 'MTCYB'] ,
	'ND1': ['NAD1', 'MT-ND1', 'MTND1', 'NADH1', 'ND1'] ,
	'ND2': ['NAD2', 'MT-ND2', 'MTND2', 'NADH2', 'ND2' ] ,
	'ND3': ['NAD3', 'MT-ND3', 'MTND3', 'NADH3', 'ND3'] ,
	'ND4': ['NAD4', 'MT-ND4', 'MTND4', 'NADH4', 'ND4'] ,
	'NDL': ['NADL','MT-ND4L', 'MTND4L', 'NADH4L', 'ND4L', 'NDL', 'NAD4L', 'NADHL'] ,
	'ND5': ['NAD5', 'MT-ND5', 'MTND5', 'NADH5', 'ND5'] ,
	'ND6': ['NAD6', 'MT-ND6', 'MTND6', 'NADH6', 'ND6']
	}
		  

def skip_atp8_nematodes(organism, file, names):
	if organism == 'cel' and file.upper()[:file.find('.')] in names.get('ATP8', []):
		print("Warning")
		return True
	return False
	
	
skip_atp8_nematodes(organism, file, names)
