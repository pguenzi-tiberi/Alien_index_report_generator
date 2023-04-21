#!/usr/bin/env python3

import argparse
import os
import sys
import time
import shutil
import pandas as pd
from sympy import im 
from lib import merging
from lib import prepare
from lib import separiting_file


def run() :
    parser = argparse.ArgumentParser(
        prog="AiRG",
        description="\n\n Alien index report Generator to detect HGT ",
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=True,
    )

    mandatory_args = parser.add_argument_group("Mandatory arguments")

    # Mandatory arguments

    # Trinotate report
    
    mandatory_args.add_argument(
        "--report",
        action="store",
        dest="blast_report ",
        help="blast (-outfmt 6) or diamond (--outfmt 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send slen evalue bitscore sskingdoms sphylums sscinames staxids skingdoms salltitles) report",
        default="",
        required=True,
    )

    mandatory_args.add_argument(
        "--id",
        action="store",
        dest="id_prot",
        help="a file (as in test directory) with only id protein (in one copy)",
        default="",
        required=True,
    )

    mandatory_args.add_argument(
        "--kingdom",
        action="store",
        dest="kingdom",
        help="The kingdom of your organism. It has to be written as in your blast / diamond report",
        default="",
        required=True,
    )
    
    optional_args = parser.add_argument_group("Optional arguments")

    # Output
    optional_args.add_argument(
        "--output",
        "-o",
        action="store",
        dest="output_dir",
        help="Output directory name",
        default="results",
        required=False,
    )

    args = parser.parse_args()

    try:
        os.mkdir(args.output_dir)
    except:
        print(
            f"\n Output directory {args.output_dir} can not be created, please erase it before launching the programm !"
        )
        sys.exit(1)

    actual_path = os.getcwd()
    os.chdir(args.output_dir)

    global_start = time.perf_counter()
    list_path_file_protein_report = separiting_file.separiting(args.blast_report,args.id_prot)

    print(
        f"\n Total running time : {float(time.perf_counter() - global_start)} seconds"
    )
            
    number_of_protein=pd.read_csv(args.id_prot, sep="\t", header=None)
    
    for sample in range (0,number_of_protein.shape[0]):

    
if __name__ == '__main__':
    run()