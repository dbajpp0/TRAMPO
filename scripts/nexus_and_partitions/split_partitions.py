from Bio.Nexus import Nexus
import sys

script_name, input, output = sys.argv
aln = Nexus.Nexus()
aln.read(input)
aln.write_nexus_data_partitions(filename=output, charpartition=aln.charsets)
