#!/usr/bin/env python3

import argparse
import os
import sys
import time
import shutil
from isort import file
import pandas as pd 
import math



def writing_alien_index_report( list_path_file_protein_report : list , number_of_prot : file , kingdom : chr) -> list:
    first_line_final_report="Gene_ID\tgene_ID_best_hit\tAI_index\t%_of_ID\tbest_hit_evalue\tBest_hit_evalue_kingdom\tBest_hit_kingdom\tbest_hit_others\tName_of_protein"
    list_line_new_file=[]
    list_line_new_file.append(first_line_final_report)

    for sample in range(0,len(list_path_file_protein_report)):

        blast_report_sample=pd.read_csv(list_path_file_protein_report[sample], sep="\t", header=None)
        blast_report_sample[12]=blast_report_sample[12].apply(float)
        blast_report_sample_sorted_by_evalue=blast_report_sample.sort_values(by=[12],ascending=True,ignore_index=True)
        match_kingdom=blast_report_sample_sorted_by_evalue[blast_report_sample_sorted_by_evalue[18] == str(kingdom)].index.values
        match_other=blast_report_sample_sorted_by_evalue[blast_report_sample_sorted_by_evalue[18] != str(kingdom)].index.values
        print(blast_report_sample_sorted_by_evalue)

        if len(match_kingdom) != 0:
            best_match_kingdom = match_kingdom[0]
            evalue_best_match_kingdom=blast_report_sample_sorted_by_evalue.iloc[best_match_kingdom,12]
            best_hit_kingdom_organism=str(blast_report_sample_sorted_by_evalue.iloc[best_match_kingdom,18])+";"+str(blast_report_sample_sorted_by_evalue.iloc[best_match_kingdom,16])
        else:
            evalue_best_match_kingdom=1
            best_hit_kingdom_organism="No hits"
            best_match_kingdom = 99.99
        if len(match_other) != 0:
            best_match_other = match_other[0]
            evalue_best_match_other = blast_report_sample_sorted_by_evalue.iloc[best_match_other,12]
            best_hit_other_organism=str(blast_report_sample_sorted_by_evalue.iloc[best_match_other,18])+";"+str(blast_report_sample_sorted_by_evalue.iloc[best_match_other,16])
        else:
            evalue_best_match_other = 1
            best_hit_other_organism="No hits"
            best_match_other = 99.99

        gene_ID=blast_report_sample_sorted_by_evalue.iloc[0,1]
        AI=math.log(evalue_best_match_kingdom+1e-200)-math.log(evalue_best_match_other+1e-200)
        best_hit_evalue_kingdom=evalue_best_match_kingdom
        
        if best_match_kingdom < best_match_other :
            gene_ID_best_Hit=gene_ID=blast_report_sample_sorted_by_evalue.iloc[best_match_kingdom,1]
            percentage_of_identity=blast_report_sample_sorted_by_evalue.iloc[best_match_kingdom,3]
            best_hit_evalue=blast_report_sample_sorted_by_evalue.iloc[best_match_kingdom,12]
            Name_of_protein=str(blast_report_sample_sorted_by_evalue.iloc[best_match_kingdom,19])
        if best_match_kingdom > best_match_other :
            gene_ID_best_Hit=blast_report_sample_sorted_by_evalue.iloc[best_match_other,1]
            percentage_of_identity=blast_report_sample_sorted_by_evalue.iloc[best_match_other,3]
            best_hit_evalue=blast_report_sample_sorted_by_evalue.iloc[best_match_other,12]
            Name_of_protein=str(blast_report_sample_sorted_by_evalue.iloc[best_match_other,19])
                
        text_new_line_for_final_report=str(gene_ID)+"\t"+str(gene_ID_best_Hit)+"\t"+str(AI)+"\t"+str(percentage_of_identity)+"\t"+str(best_hit_evalue)+"\t"+str(best_hit_evalue_kingdom)+"\t"+str(best_hit_kingdom_organism)+"\t"+str(best_hit_other_organism)+"\t"+str(Name_of_protein)
        list_line_new_file.append(text_new_line_for_final_report)

    return list_line_new_file


def writting_file( list_line_new_file : list ) :
    final_report=open("final_report.tsv", "w")  # write mode
    for sample in range(0,len(list_line_new_file)):
        final_report.write(str(list_line_new_file[sample])+"\n")
    final_report.close()