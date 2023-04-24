#!/usr/bin/env python3

import argparse
import os
import sys
import time
import shutil
from isort import file
import pandas as pd 


def writing_alien_index_report( list_path_file_protein_report : list , number_of_prot : file , kingdom : chr) -> file:
    list_line_new_file=[]
    for sample in range(0,len(list_path_file_protein_report)):
        blast_report_sample=pd.read_csv(list_path_file_protein_report[sample], sep="\t", header=None)
        blast_report_sample[12]=blast_report_sample[12].apply(float)
        print(blast_report_sample)
        blast_report_sample_sorted_by_evalue=blast_report_sample.sort_values(by=[12],ascending=True)
        print(blast_report_sample_sorted_by_evalue)
        match_kingdom=blast_report_sample_sorted_by_evalue.iloc(blast_report_sample_sorted_by_evalue[17] == str(kingdom)).index.values
        match_other=blast_report_sample_sorted_by_evalue.iloc(blast_report_sample_sorted_by_evalue[17] != str(kingdom)).index.values
        if len(match_kingdom) != 0:
            best_match_kingdom = match_kingdom[0]
        else:
            best_match_kingdom = 1
        if len(match_other) != 0:
            best_match_other = match_other[0]
        else:
            best_match_other = 1
        print(best_match_kingdom, "\t", best_match_other)
    return "lol"