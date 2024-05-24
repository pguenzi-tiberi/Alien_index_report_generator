# Generator of Alien index to detect HGT

It is a small python program to compute alien index, create a report table and analyse that. So you can use it, modify it etc !

## Command example

To generate the good report, you can use a similar command line :

`diamond blastp --db nr_db --threads 32 -q ./proteins_file --out report_blast.tsv --outfmt 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send slen evalue bitscore sskingdoms sphylums sscinames staxids skingdoms salltitles -e 0.0001 --ultra-sensitive --max-target-seqs 800 `

Then, you have to generate the `lis_id_prot_fungi_uniq` file :

`awk -F "\t" '{print $1}' report_blast.tsv | sort| uniq > lis_id_prot_fungi_uniq`

`sort -k1 report_blast.tsv > report_blast_sorted.tsv`

Finally : 

`Alien_index_report_generator --report /abspath/report_blast_sorted.tsv --id /abspath/lis_id_prot_fungi_uniq --kingdom Fungi`

The different kingdom which can be used by this file are :

- Fungi

- Viridiplantae

-  Bacteria (This kingdom brings together archaea and bacteria. You have to write 0 (zero) in the command line)

-  Metazoa
