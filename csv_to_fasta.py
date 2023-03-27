#!/usr/bin/env python
'''
************ Bioinformatics: Research Project ************
***  Small python script to convert the csv file with the data into a FASTA  ***
Author(s): Joel Moreira
Description: A parser that reads the csv  file with the input dataand outputs a fasta file
with the header (containing the gcf/acc/specie/strain) and the sequence
Usage: ./csv_to_fasta.py [input] [output]
Example: ./csv_to_fasta.py firmicutes_table_1e-70-80_with_seq_v7.csv firmicutes.fa
'''
import csv
import sys
inputPath = sys.argv[1]
outputPath = sys.argv[2]
print(
"\n"
"###########
######\n"
"...\n"
"...\n"
"..."
)
n = 18
The header will contain the gcf, acc, specie and strain of each seq
#####
with open(inputPath, 'r') as csvFile:
reader = csv.reader(csvFile, delimiter = '\t')
next(reader)
with open(outputPath, 'w') as outfas:
for row in reader:
n += 1
gcf = row[0]
acc =row[1]
specie = row[17]
specie= specie.replace(" ","-")
strain = row [18]
strain= strain.replace(" ","-")
dnaseq = row[8]
outfas.write('>' + gcf + '' + acc + ''+ specie + '_' + strain + '\n' + dnaseq + '\n')
print(
"###########     Task Done Sucessfully   ###########\n")
