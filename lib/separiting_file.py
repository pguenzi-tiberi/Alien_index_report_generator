#!/usr/bin/env python3

import argparse
import os
import sys
import time
import shutil
from isort import file
import pandas as pd 

def separiting (blast_report : file, id_prot : file) -> list:
    table_blast = pd.read_csv(blast_report, sep="\t", header=None)
    number_of_protein=pd.read_csv(args.id_prot, sep="\t", header=None)
    list_path_file_prot_blast=[]
    counter=0
    for sample in range(0,number_of_protein.shape[0]):
        counter+=1
        if sample == len(line_gene)-1 :
            small_gene_df=table_gff.iloc[line_gene[sample]:-1,]
        if sample == len(line_gene)-2 :
            small_gene_df=table_gff.iloc[line_gene[sample]:line_gene[-1],]
        else :
            small_gene_df=table_gff.iloc[line_gene[sample]:line_gene[sample+1],]
        small_gene_df.to_csv(path_or_buf="mini_gff"+str(counter), sep="\t", header=False)
        list_path_file_prot_blast.append(os.path.abspath("mini_gff"+str(counter)))
    return     list_path_file_prot_blast