#!/bin/bash

output_path="$1"
gene_order="$2"

output_folders_w_strand=(
    'tmp' '01_Original_Files' '02_Corrected_Files' 'Alignment' '03_Nexus' '03_Nexus/NT' '03_Nexus/AA'
    '04_Domains_Nexus_per_Gene' '04_Domains_Nexus_per_Gene/TM' '04_Domains_Nexus_per_Gene/IM' '04_Domains_Nexus_per_Gene/MA'
    '04_Domains_Nexus_per_Strand' '04_Domains_Nexus_per_Strand/TM' '04_Domains_Nexus_per_Strand/IM' '04_Domains_Nexus_per_Strand/MA'
    '05_Tables' '06_Stat' '07_Graphics' '08_Partition_files'
)

output_folders=(
    'tmp' '01_Original_Files' '02_Corrected_Files' 'Alignment' '03_Nexus' '03_Nexus/NT' '03_Nexus/AA'
    '04_Domains_Nexus_per_Gene/TM' '04_Domains_Nexus_per_Gene/IM' '04_Domains_Nexus_per_Gene/MA'
    '05_Tables' '06_Stat' '07_Graphics' '08_Partition_files'
)

if [ -d "$output_path" ]; then
    rm -rf "$output_path"
fi

# Create output_path
mkdir -p "$output_path"

# Select appropriate output_folders based on gene_order
if [ "$gene_order" -eq 1 ]; then
    output_folders_to_use=("${output_folders_w_strand[@]}")
else
    output_folders_to_use=("${output_folders[@]}")
fi

# Create subdirectories
for folder in "${output_folders_to_use[@]}"; do
    mkdir -p "$output_path/$folder"
done
