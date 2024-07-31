import sys
import os

script_name, path = sys.argv

print('Standardizing file names...')

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
	
	
# mtDNA files should be 13, if less print a warning
num_files = len(os.listdir(path))
if num_files < 13:
	print('Warning:', num_files, 'files detected in' , path)

for file in os.listdir(path):
	original_file_path = os.path.join(path, file)

	# Check if the item in the directory is a file
	if os.path.isfile(original_file_path):
		for standard_name, variations in names.items():
			# Check if the file name (without extension) matches any variation
			if file[:file.find('.')].upper() in variations:
				new_file_name = standard_name.lower() + '.fa'
				new_file_path = os.path.join(path, new_file_name)

				# Check if the new file name already exists
				if not os.path.exists(new_file_path):
					os.rename(original_file_path, new_file_path)
					print(f'Renamed: {file} to {new_file_name}')

print('File names correctly renamed!')
