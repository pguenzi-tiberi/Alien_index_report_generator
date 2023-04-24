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
    number_of_protein=pd.read_csv(id_prot, sep="\t", header=None)
    list_path_file_prot_blast=[]
    counter=0
    for sample in range(0,number_of_protein.shape[0]-1):
        counter+=1
        if sample == number_of_protein.shape[0]-1 :
            line_gene=table_blast[table_blast[0]==number_of_protein[0][sample]].index.values[0]
            small_gene_df=table_blast.iloc[line_gene:-1,]
        if sample == number_of_protein.shape[0]-2 :
            line_gene=table_blast[table_blast[0]==number_of_protein[0][sample]].index.values[0]
            line_gene_2=table_blast[table_blast[0]==number_of_protein[0][sample+1]].index.values[0]
            small_gene_df=table_blast.iloc[line_gene:line_gene_2,]
        else :
            line_gene=table_blast[table_blast[0]==number_of_protein[0][sample]].index.values[0]
            line_gene_2=table_blast[table_blast[0]==number_of_protein[0][sample+1]].index.values[0]
            small_gene_df=table_blast.iloc[line_gene:line_gene_2,]
        small_gene_df.to_csv(path_or_buf="mini_blast_report"+str(counter), sep="\t", header=False)
        list_path_file_prot_blast.append(os.path.abspath("mini_blast_report"+str(counter)))
    return list_path_file_prot_blast