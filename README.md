
# TRAMPO v.2024.1

TRAMPO (TRAnsMembrane Protein Order) is a fast and automized pipeline designed to study nucleotide composition in trans-membrane, matrix and inner matrix space regions from multiple mitochondrial protein coding gene (PCG) sequences of several species. TRAMPO goal is to obtain a NEXUS file containing region-partitions at three different levels (codon, strand, and trans-membrane regions) to employ in phylogenetic studies.

In brief, by taking in (i) input FASTA files of mitochondrial genes, (ii) the correspondent genetic code and (iii) the closest model organism, the program:

	

	

	

A manuscript describing the results that can be obtained with this pipeline can be downloaded from bioRxix XXXXXXXXXXXXXXXXXXXXX

	

	

Trempó (pronounced trəmˈpo in Catalan), and incorrectly spelled trampó in Spanish, is a Mallorcan summer salad made with pale green pepper, tomato and onion and dressed with salt and extra virgin olive oil. The colors of its ingredients blends those in the Italian flag.

	

	

In brief, by taking in (i) input FASTA files for each of the 13  mitochondrial PCGs, (ii) the correspondent genetic code and (iii) the closest model organism, the program: 
 1. Checks the input files
 2. Align ingroups *plus* the chosen model species
 3. Splits the protein regions in three domain (TM: Transmebrane, MA: Mitochdondrial matrix, IM: Inner Mitochondrial Space) following the chosen model organism domain prediction table
 4. Creates graphics, statistics and a NEXUS charset file partitioned per codon, gene and domain (TM, MA, IM) 


# License
GNU GENERAL PUBLIC LICENSE. Version 3, 29 June 2007



# Requirements

Linux OS
Conda (https://docs.conda.io/)

We recommend to update/upgrade your system before installing the pipeline:
 `sudo apt update`
 `sudo apt upgrade`


# Installation
Just copy paste the following commands in your terminal
```
# Download the program from GitHub
$ git clone https://github.com/TRAMPO

# Unzip the archive and move in the unzipped folder
$ unzip TRAMPO.zip | cd TRAMPO

# Create the conda environment -- user does not need to install dependecies alone --
$ conda env create -f TRAMPO.yml

# "Step-in" the environment
$ conda activate TRAMPO

# Make it executable
$ chmod +x TRAMPO

# Copy the program in the environment PATH and make it executable
$ cd .. && sudo cp -r TRAMPO /usr/local/bin/

# Open with a text editor (i.e. nano or vim) file the .bashrc file...
$ nano ~/.bashrc
# ...and append the following string at the end of the file and save
$ export PATH=$PATH:/usr/local/bin/TRAMPO
```

# Getting started

As the `--help` or `-h` argument suggests, TRAMPO requires three **mandatory** parameters:

 - The path to mitochondrial sequences in FASTA format (`-p`,`--path`)
 - The genetic code (following the [NCBI Genetic Codes](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi)) (`-c`, `--code`)
 - The model organism nickname (to be chosen from the available list) (`-m`, `--model`)

and four **optional** parameters:

 - The path to customized user's processed output TMHMM tables (`-t`,`--tables`)
 - The corresponding FASTA file of mitochondrial genes (used to generate TMHMM output tables) (`-s`,`--sequence`)
 - The output directory (`-o`,`--outdir`)
 - The gene order model nickname to be employed during the analysis. It should be choosen according to the passed model organism (see `-m` option) (`-go`,`--gene_order`)
 - The threads number to be employed during the MAFFT alignment
```
$ trampo -h

Usage: trampo [-p PATH-TO-FILES] [-c GENETIC-CODE] [-m MODEL] [OPTIONS]

TRAMPO version 2024.8

REQUIRED:
  -p, --path  PATH    Path to fasta files directory [required]
  -c, --code  INT     Genetic code [Integer] referred as in NCBI https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi (e.g., 5 invertebrates mitochondrial) [required]
  -m, --model STR     Nickname of the default model organism [required]
                         User table (if you pass -s and -t): user
                         Homo sapiens (Mammalia): hsa
                         Lycodon semicarinatus (Lepidosauria): lse
                         Gallus gallus (Aves): gga
                         Xenopus leavis (Amphibia): xle
                         Danio rerio (Actinopterygii): dre
                         Scyliorhinus canicula (Chondrichthyes): sca
                         Petromyzus marinus (Agnatha): pma
                         Patiria pectinifera (Asteroidea) ppe
                         Strongylocentrotus purpuratus (Echinoidea): spu
                         Drosophila melanogaster (Pancrustacea): dme
                         Rhipicephalus sanguineus (Chelicerata): rsa
                         Albinaria caerulea (Mollusca): aca
                         Lumbricus terrestris (Anellida): lte
                         Caenorhabditis elegans (Nematoda): cel
                         Metridium senile (Cnidaria): mse

OPTIONAL SETTINGS:
  -s, --sequence      FASTA   User's model organism genes file in FASTA format. Check the manual for instructions
  -t, --tables        PATH    Path to user's model organism table files in TMHMM format. Check the manual for instructions
  -o, --outdir        PATH    Output directory (default: 'outdir')
  -g, --gene_order    STR     Gene order model nickname to be employed during the analysis, according to the proposed model organisms (see -m parameter). Check the manual for further information.
                                  All vertebrates: vert
                                  Arthropods: panc
                                  Lumbricus terrestris, Caenorhabditis elegans, Metridium senile: ances
                                  Albinaria caerulea: albin
  -n, --threads       INT     Number of threads to employ in MAFFT (default: 1)

MISCELLANEA:
  -h, --help		Display this help and exit
  -v, --version	Display version information and exit


```


# To those who can't wait

```
$ trampo -p /path/to/your/fasta/files -c number_of_genetic_code -m closest_model_organism_nickname
 ```
For example:

 ```
 trampo -p examples/Primates -c 2 -m hsa 
 ```


# Basic analyses (recommended)

## Launch TRAMPO choosing a default model organism

In order to properly work, TRAMPO requires **the path to fasta sequence files** (`-p`) containing multiple species mitochondrial genes as **nucleotide sequences**. An example on how it should be arranged the FASTA file you can check the `examples` folder of the program. By the way, we also report and example here:
```
Genes_folder
		|_____________cox1.fa
		              cox2.fa
		              cox3.fa
		              cytb.fa
		              atp6.fa
		              atp8.fa
		              nd1.fa
		              nd2.fa
		              nd3.fa
		              nd4.fa
		              ndl.fa
		              nd5.fa
		              nd6.fa
```
It is **mandatory** to rename the files as the gene name, following one of these alternatives (upper-lower case is not significant):
|Gene|Accepted nomenclature
|--|--|
|ATP6|ATP6, A6, MT-ATP6, ATPASE6
|ATP8  |A8, ATP8,MT-ATP8, ATPASE8
|COX1| MT-CO1, CO1, COX1, COXI, MTCO1, MTCOX1, MTCOXI     
|COX2| MT-CO2, CO2, COX2, COXII, MTCO2, MTCOX2, MTCOXII
|COX3| MT-CO3, CO3, COX3, COXIII, MTCO3, MTCOX3, MTCOXIII
|CYTB| MT-CYB, COB, CYTB, MTCYB
|ND1| MT-ND1, MTND1, NADH1, ND1, NAD1
|ND2| MT-ND2, MTND2, NADH2, ND2, NAD2
|ND3| MT-ND3, MTND3, NADH3, ND3, NAD3
|ND4| MT-ND4, MTND4, NADH4, ND4, NAD4
|NDL| MT-ND4L, MTND4L, NADH4L, ND4L, NAD4L
|ND5| MT-ND5, MTND5, NADH5, ND5, NAD5
|ND6| MT-ND6, MTND6, NADH6, ND6, NAD6


Moreover, the user has to pass also the corresponding **genetic code** (`-c`) argument following the [NCBI tables](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi)

Finally, a species nickname (`-m`) is required and it should be chosen depending on the employed dataset (e.g. if Hominidae are analysed, therefore `hsa` should be passed)
```
Homo sapiens (Chordata): hsa
Patiria pectinifera (Echinodermata) ppe
Drosophila melanogaster (Pancrustacea+Chelicerata): dme
Albinaria caerulea (Mollusca): aca
Lumbricus terrestris (Anellida): lte
Caenorhabditis elegans (Nematoda): cel
Metridium senile (Cnidaria): mse
```
If any of the above mentioned model organism fit with user's purposes, check [below](#Advanced-analysis) on how to customize the pipeline with optional parameters.

#### Example
    $ trampo -p examples/Primates -c 2 -m hsa

In this example we are using  Protein Coding Gene sequences from primates, therefore the choice of the genetic code will be the **second** (Vertebrate mitochondrial). In addition, the model organism to employ in the pipeline will be *Homo sapines* (`hsa`) due to the closer phylogenetic proximity to monkeys. 

# Advanced analyses 

## Launch TRAMPO with custom model organism

TRAMPO relies on its speed thanks to default model organism trans-membrane prediction tables loaded in the folder program. User can take advantage from it by selecting the phylogenetically closer model orgranism from the one proposed in the list (see [above](#launch-trampo-choosing-a-default-model-organism) or can load his/her own customized prediction tables obtained from the TMHMM software (or equally formatted) altogether with the corresponding FASTA sequences.

In this case, user **must pass** `user` in the `-m` option  (i.e. `-m user`)

The parameter `-t` or `--tables` takes the path to **text** files containing the copy-pasted TMHMM output tables. The folder should be arranged as follows:


    TMHMM_tables
        |_____________cox1_tmhmm.txt
                      cox2_tmhmm.txt
                      cox3_tmhmm.txt
                      cytb_tmhmm.txt
                      atp6_tmhmm.txt
                      atp8_tmhmm.txt
                      nd1_tmhmm.txt
                      nd2_tmhmm.txt
                      nd3_tmhmm.txt
                      nd4_tmhmm.txt
                      ndl_tmhmm.txt
                      nd5_tmhmm.txt
                      nd6_tmhmm.txt

It is **mandatory** to rename the files as the gene name (following the admitted names for genes as reported in the table available at the [Launch TRAMPO choosing a default model organism](##Launch-TRAMPO-choosing-a-default-model-organism) section).

Each file must appear as the following example:

```
$ cat atp6.txt

    # lcl|NC_012920.1_prot_YP_003024026.1_1 Length: 318
    # lcl|NC_012920.1_prot_YP_003024026.1_1 Number of predicted TMHs:  8
    # lcl|NC_012920.1_prot_YP_003024026.1_1 Exp number of AAs in TMHs: 167.91966
    # lcl|NC_012920.1_prot_YP_003024026.1_1 Exp number, first 60 AAs:  19.37957
    # lcl|NC_012920.1_prot_YP_003024026.1_1 Total prob of N-in:        0.36409
    # lcl|NC_012920.1_prot_YP_003024026.1_1 POSSIBLE N-term signal sequence
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	outside	     1     3
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	TMhelix	     4    23
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	inside	    24    67
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	TMhelix	    68    90
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	outside	    91    99
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	TMhelix	   100   122
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	inside	   123   134
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	TMhelix	   135   157
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	outside	   158   171
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	TMhelix	   172   191
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	inside	   192   221
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	TMhelix	   222   244
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	outside	   245   253
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	TMhelix	   254   273
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	inside	   274   292
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	TMhelix	   293   315
    lcl|NC_012920.1_prot_YP_003024026.1_1	TMHMM2.0	outside	   316   318
```
Altogether with the path to table files it is **mandatory** to pass the `-s` `--sequence` FASTA file containing the **aminoacid** sequences of the users' model organism. FASTA sequences must contain the gene name as header, following the table reported in [Launch TRAMPO choosing a default model organism](##Launch-TRAMPO-choosing-a-default-model-organism) as accepted names.

    $ head Pan_panicus.fna

    >nad1_ppa
    TPMTNLLLLIVPVLIAMAFLMLTERKILGYMQLRKGPNIVGPYGLLQPFADAMKLFTKEPLKPSTSTITL
    YITAPTLALTIALLLWTPLPMPNPLVNLNLGLLFILATSSLAVYSILWSGWASNSNYALIGALRAVAQTI
    SYEVTLAIILLSTLLMSGSFNLSTLITTQEHLWLILPTWPLAMMWFISTLAETNRTPFDLTEGESELVSG
    FNIEYAAGPFALFFMAEYMNIIMMNTLTATIFLGTTYNTHSPELYTTYFVTKALLLTSLFLWIRTTYPRL
    CYDQLMHLLWKNFLPLTLASLMWYISMPTTISSIPPQT
    >nad2_ppa
    MNPLAQPIIYSTIFAGTFITVLSSHWFFTWVGLEMNMLAFIPVLTKKMSPRSTEAAIKYFLTQATASMIL
    LMAILSNNMLSGQWTMTNTTNQYSSLMIMTAMAMKLGMAPFHFWVPEVTQGTPLMSGLLLLTWQKLAPIS
    IMYQMSSSLNVNLLLTLSILSIMAGSWGGLNQTQLRKILAYSSITHMGWMMAVLPYNPNMTILNLTIYII
    LTTTTFLLLNLNSSTTTLLLSRTWNKLTWLTPLIPSTLLSLGGLPPLTGFLPKWVIIEEFTKNNSLIIPT
    TMAIITLLNLYFYLRLIYSTSITLLPMSNNVKMKWQFEHTKPTPFLPTLITLTTLLLPISPFMLMIL

#### Example
    $ trampo -p examples/Primates -c 2 -t examples/TMHMM_tables -s examples/Pan_panicus.fna -m user

If the user wish to launch TRAMPO using an own custom model organism, it is necessary to add both the path to TMHMM tables and the correspondent model organism sequences in FASTA format. Moreover you need to pass `user` as `-m` argument.

Using this option, TRAMPO will rely on custom sequences following the domain tables provided.

## Launch TRAMPO with the gene order variable

TRAMPO was though to split mitochondrial Protein Coding Genes according to their protein domain. However, a different mutation rate can be observed by partitioning the matrices by strand (Heavy and Light - Positive and Negative chains). For this reason, TRAMPO offers the choice to pass an option argument `-go` or `--gene_order` by selecting the most closest gene arrangement from an available list:

```
All vertebrates: vert
Arthropods: panc
Lumbricus terrestris, Caenorhabditis elegans, Metridium senile: ances
Albinaria caerulea: albin
Metacangronyx: meta
```
to obtain a partitioning scheme adapted to positive and negative chain, deprecating the gene identity.


In detail the corresponding gene arrangements are:

**Albinaria caerulea - albin**
|   |  | |  | |  ||  | |  |
|--|--|--|--|--|--|--|--|--|--|
|Positive chain  | nad1| nad2|nad4|nadl|nad5|nad6|cox1|cox2|cytb
|Negative chain  |  nad3|cox3|atp6|atp8

**Lumbricus terrestris, Caenorhabditis elegans, Metridium senile - ances**
|  |  | |  | |  ||  | |  |||||
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|Positive chain  | nad1|nad2|nad3|nad4|nadl|nad5|nad6|cox1|cox2|cox3|cytb|atp6|atp8|
|Negative chain 

**Arthropods - panc**
|  |  | |  | |  ||  | |  ||
|--|--|--|--|--|--|--|--|--|--|--|
|Positive chain|nad2|nad3|nad4|nad6|cox1|cox2|cox3|cytb|atp6|atp8|
|Negative chain| nad1|nad4|nadl|nad5

**Vertebrate - vert**
|  |  | |  | |  ||  | |  ||||
|--|--|--|--|--|--|--|--|--|--|--|--|--|
|Positive chain  | nad1|nad2|nad3|nad4|nadl|nad5|cox1|cox2|cox3|cytb|atp6|atp8|
|Negative chain | nad6

To use a custom gene order, please add a file to the `templates/go/` folder, rename it as you wish but **without extension** and pass this name to the `-go` option
Example:

    $ echo "positive:nad3,nad4,nadl,nad5,cox1,cox2,cox3,cytb,atp6,atp8" > templates/go/mycustomgo
    $ echo "negative:nad1,nad2,nad6" >> templates/go/mycustomgo
    
    $ trampo -p myFolder -c 2 -m hsa -go mycustomgo
    



# What TRAMPO does?

The primary goal of the pipeline is to release a NEXUS partition file, useful to run in phylogenetic softwares (e.g. IQTREE), splitted in charsets related to the membrane position of processed Protein Coding Genes.

 * Firstly, it performs a quality check of both required and (if passed) optional input files. In detail:
   * To sequences within the folder passed with the `-p` or `--path` argument:
     * It checks if they are in FASTA format, otherwise it automatically converts them in FASTA printing a **Warning**.
     * It replaces special chararcters (if any) in their headers.
     * It checks for dulicated IDs (if any) and renames duplicated headers.
     * It checks if they are nucleotide or aminoacid sequences. It only accepts **nucleotides**, otherwise the pipeline stops with an **Error** message.
     * It assesses their length and, if any sequence is longer or shorter than the median+/-(stdev*3) than the rest, prints a **Warning** message.
     * It looks for stop codons. If only one is present, the script trims the sequence in that position. If multiple stop codons are present, the pipeline stops printing an **Error** message.
   * To gene order optional argument, passed with the `-g` or `--gene_order`:
     * Undergoes to a control to check if the required syntax is respected
   * To custom gene sequences optional argument, passed with the `-s` or `--sequence`:
     * TRAMPO checks if they are in FASTA format, otherwise converts them into FASTA printing a **Warning** message.
     * Cheks if multiple stop codons are present. If only one is retrieved at the end of the sequence it trims it. Otherwise, if multiple stop codons and/or not terminal stop codon is found the pipeline stops by priting an **Error** message. For this reason we recommend to use RefSeq mitochondtial CDSs.
     * Checks if the user also passed the corresponding tables (see the next point).
   * To custom and optional TMHMM tables, passed with the `-t` `--tables` argument:
     * The pipeline controls the intrgrity of the files that should respect the formatting requirments above explicate (#Launch-TRAMPO-with-custom-model-organism)
 
_Note: at this step, all original files are stored in a folder named 1_Original_Files, whereas corrected files are placed in a working directory named 2_Corrected_Files_
   
* After this sanity check, TRAMPO individually aligns amicnoacid sequences in a temporary files trough `MAFFT` v7.475.
* Depending on the model organism you selected (through the `-m` option), TRAMPO adds the corresponding model organism reference gene to the ingroup alignment and re-aligns the entire dataset via `MAFFT` v7.475 depending on the `--add` parameter. The resulting alignment is then back translated to nucleotides.
* Alignments are then individually converted in NEXUS format via `EMBOSS seqret` v6.5.7.0 and concatenated in a supermatrix following the alphabetical order trough `catsequences`. This file is named as `nt_combined.nex`.

_Note: at this step, all NEXUS files are placed in a working directory named 4_Nexus_

* At this point, each alignment is sliced in different charset partitions - TM (transmembrane), IM (inner mitochondrial space) and MA (mitochondrial matrix) - **depending on the reference sequence and the corresponding table which delimits these domains**. It means that, if the model organism sequence is shorter than ingroups, then ingroup sequences will be truncated. Further, only gap columns and model organism reference sequences are removed. At the end of this process, each NEXUS matrix is composed of three charsets.
* Subsequently, TRAMPO reformats the domain charsets by handling these matrices. It creates up to 7 different NEXUS partition files:
  * new_charsets_codons.nex
  * new_charsets_genes.nex
  * new_charsets_genes_regions.nex
  * new_charsets_regions_codons.nex
  * new_charsets_regions.nex
  * new_charsets_codons_strand.nex (if `-g` was defined)
  * new_charsets_strand_regions.nex  (if `-g` was defined)

_Note: at this step, all NEXUS files are stored in the main output folder_

* Each partition file is then employed to split the concatenated supermatrix, obtaining 39 different working NEXUS files (i.e. each gene is splitted for IM, MA and TM regions).

 _Note: at this step, splitted NEXUS files are stored in 5_Domains_Nexus_per_Gene and (in `-g` was passed) 5_Domains_Nexus_per_Strand_

* Then, the combined NEXUS file with appended partitions undergoes a series of calculations, as:
  * Aminoacid frequency
  * Relative Synonym Codon Usage
  * GC frequency (First skew)
  * AT-CG skew (Second and Third skew)

_Note: at this step, all TSV files are stored in the 6_tables folder_


* Each table is processed to produced a the mean and the standard deviation by regions and (if `-g` was defined) by strand (chain). Obtaining the following TSV tables:
  * AminoAcid_frequency_by_chain_mean-stdev-test.tsv (if `-g` was defined)
  * AminoAcid_frequency_by_chain_wilcoxon-test.tsv (if `-g` was defined)
  * AminoAcid_frequency_by_region_mean-stdev-test.tsv
  * AminoAcid_frequency_by_region_wilcoxon-test.tsv
  * GC_frequency_by_chain_mean-stdev-test.tsv (if `-g` was defined)
  * GC_frequency_by_chain_wilcoxon-test.tsv (if `-g` was defined)
  * GC_frequency_by_region_mean-stdev-test.tsv
  * GC_frequency_by_region_wilcoxon-test.tsv
  * RSCU_by_chain_mean-stdev-test.tsv (if `-g` was defined)
  * RSCU_by_chain_wilcoxon-test.tsv (if `-g` was defined)
  * RSCU_by_region_mean-stdev-test.tsv
  * RSCU_by_region_wilcoxon-test.tsv

* Similarly, each table is in turn used to produce different plots both in HTML and PDF:
  * AminoAcid_frequency_by_chain.html (if `-g` was defined)
  * AminoAcid_frequency_by_chain.pdf (if `-g` was defined)
  * AminoAcid_frequency_by_region.html
  * AminoAcid_frequency_by_region.pdf
  * GC_frequency_by_region.html 
  * GC_frequency_by_region.pdf
  * Skew-PCA_by_chain.html (if `-g` was defined)
  * Skew-PCA_by_chain.pdf (if `-g` was defined)
  * Skew-PCA_by_region.html
  * Skew-PCA_by_region.pdf

_Note: at this step, all TSV statistical files are stored in the 7_Stat, whereas graphical outputs are placed in 8_Graphics folder_


### Outputs

Outputs will be saved in an out directory `outdir` (or the custom user's name passed via `-o` option). Inside the `outdir`, if any error occurred, you will find the following output folders:
```
$ tree -d outdir

outdir
├── 1_Original_Files
├── 2_Corrected_Files
├── 3_Nexus
│   ├── AA
│   └── NT
├── 4_Domains_Nexus_per_Gene
│   ├── IM
│   ├── MA
│   └── TM
├── 5_Tables
├── 6_Stat
└── 7_Graphics
```

and, if `-g` was passed:

```
outdir
├── 1_Original_Files
├── 2_Corrected_Files
├── 3_Nexus
│   ├── AA
│   └── NT
├── 4_Domains_Nexus_per_Gene
│   ├── IM
│   ├── MA
│   └── TM
├── 4_Domains_Nexus_per_Strand
│   ├── IM
│   ├── MA
│   └── TM
├── 5_Tables
├── 6_Stat
└── 7_Graphics
```

Folder numbers follows the chronological order of TRAMPO commands. In this respect,

 - `1_Original_Files` contains a copy of the files passed with the `-p` or `--path` argument
 - `2_Corrected_Files` contains the nucleotide and aminoacidic corrected sequences
 - `4_Nexus` contains the NEXUS concatenated file of all the analyzed genes _plus_ NEXUS files with partitioned schemes (IM, MA, TM). This folder is divided into two subfolder `AA` and `NT` containing, respectively, aminoacid and nucleotide sequences. 
 - `5_Domains_Nexus_per_Gene` contains thhree subfolders `IM`, `MA`, `TM` where splitted matrices by genes in NEXUS format are stored.
 - `5_Domains_Nexus_per_Strand` contains thhree subfolders `IM`, `MA`, `TM` where splitted matrices by chains in NEXUS format are stored.
 - `6_Tables` contains the TSV tables of amino-acid frequency, first and second skews and RSCU
 - `7_Stat` contains the TSV files with simple statistics (mean, standard deviation) and the MW-test for each of the computed tables
 - `8_Graphics` contains the plots for each of the computed tables

Moreover, directly in the `outdir` folder, NEXUS partition files are written:
```
├── new_charsets_codons.nex
├── new_charsets_codons_strand.nex
├── new_charsets_genes.nex
├── new_charsets_genes_regions.nex
├── new_charsets_regions_codons.nex
├── new_charsets_regions.nex
└── new_charsets_strand_regions.nex
```

# What TRAMPO does not do?
- It is not a tool designed to construct phylogeny. The primary aim is to aid researchers to split their mitochondrial Protein Coding Genes accordingly to their predicted secondary structures.
- It does not split genes that does not belong to mitochodrion's genome. The use of nuclear genes is strongly not recommended.
- It does not launch the PartitionFinder or ModelFinder analyses


# Contacts
For further questions, suggestions and bugs you can email me at claudio.cucini2@unisi.it
