#!/usr/bin/env python

import fileinput
import os
import sys
import re

scrupt_name, longo, old_char = sys.argv

both=("atp6_MA","atp6_TM","atp6_IM","atp8_MA","atp8_TM","atp8_IM","cob_MA","cob_TM","cob_IM","cox1_MA","cox1_TM","cox1_IM","cox2_MA","cox2_TM","cox2_IM","cox3_MA","cox3_TM","cox3_IM","nd1_MA","nd1_TM","nd1_IM","nd2_MA","nd2_TM","nd2_IM","nd3_MA","nd3_TM","nd3_IM","nd4_MA","nd4_TM","nd4_IM","nd5_MA","nd5_TM","nd5_IM","nd6_MA","nd6_TM","nd6_IM","ndl_MA","ndl_TM","ndl_IM")
regions=("MA","TM","IM")
genes=("atp6","atp8","cob","cox1","cox2","cox3","nd1","nd2","nd3","nd4","nd5","nd6","ndl")

my_dict = {}

print('#nexus')
print('begin sets;')

with open(longo, "r") as t:
	for line in t:
		input_string = line.strip()
		nom, longitud = input_string.split("=")
		nom = re.sub(r'\W+', ' ', nom)  # Replace non-word characters with spaces
		
		# Assuming you want to extract key-value pairs from the line
		pattern = r'(\w+)=(\w+)'
		key_value_pairs = re.findall(pattern, input_string)
		my_dict.update(dict(key_value_pairs))

new_dict = {}
current_sum = 0

for key in sorted(my_dict.keys()):
	new_dict[key] = str(current_sum)
	current_sum += int(my_dict[key])

for i in range(0,len(genes)):
	f = open(old_char, "r")
	for line in f:
		if str(genes[i]+"_MA") in line:
			MA_interval = line.replace("MA=[","").replace("]","").replace("\n","").replace(genes[i],"").replace("_","")
			MA_N_interval = MA_interval.split(",")
			n = len(MA_N_interval)
			print("\tcharset ",genes[i],"_MA = ", sep="", end='')
			for j in range (0,n):
				MA_N_interval_individual = MA_N_interval[j].split("-")
				for k in range(0,1):
					LEFT_newMA_N_interval_individual = int(MA_N_interval_individual[0]) + int(new_dict.get(genes[i]))
					RIGHT_newMA_N_interval_individual = int(MA_N_interval_individual[1]) + int(new_dict.get(genes[i]))
					print(LEFT_newMA_N_interval_individual,"-",RIGHT_newMA_N_interval_individual, sep='', end='', flush=True)
				print(" ",end='')
			print(";")
		elif str(genes[i]+"_TM") in line:
			TM_interval = line.replace("TM=[","").replace("]","").replace("\n","").replace(genes[i],"").replace("_","")
			TM_N_interval = TM_interval.split(",")
			n = len(TM_N_interval)
			print("\tcharset ",genes[i],"_TM = ", sep="", end='')
			for j in range (0,n):
				TM_N_interval_individual = TM_N_interval[j].split("-")
				for k in range(0,1):
					LEFT_newTM_N_interval_individual = int(TM_N_interval_individual[0]) + int(new_dict.get(genes[i]))
					RIGHT_newTM_N_interval_individual = int(TM_N_interval_individual[1]) + int(new_dict.get(genes[i]))
					print(LEFT_newTM_N_interval_individual,"-",RIGHT_newTM_N_interval_individual, sep='', end='', flush=True)
				print(" ",end='')
			print(";")
		elif str(genes[i]+"_IM") in line:
			IM_interval = line.replace("IM=[","").replace("]","").replace("\n","").replace(genes[i],"").replace("_","")
			IM_N_interval = IM_interval.split(",")
			n = len(IM_N_interval)
			print("\tcharset ",genes[i],"_IM = ", sep="", end='')
			for j in range (0,n):
				IM_N_interval_individual = IM_N_interval[j].split("-")
				for k in range(0,1):
					LEFT_newIM_N_interval_individual = int(IM_N_interval_individual[0]) + int(new_dict.get(genes[i]))
					RIGHT_newIM_N_interval_individual = int(IM_N_interval_individual[1]) + int(new_dict.get(genes[i]))
					print(LEFT_newIM_N_interval_individual,"-",RIGHT_newIM_N_interval_individual, sep='', end='', flush=True)
				print(" ",end='')
			print(";")
		else:
			continue
print('end;')

