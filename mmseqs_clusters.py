#!/usr/bin/python3
###                      ************ Bioinformatics Master ************
###
# Date: 2022-05-12
# Author(s): Joel Moreira
*** Parser for tsv cluster file ***
# Description:
#   A parser that reads the output of mmseqs and a file created by: cat [mmseqs output]| c
ut -f1| uniq -c| sort -n > output.txt with the original input data (firmicutes table) and
 outputs the curated subfamilies and in how many different cluster they are with mmseqs.
# Usage:
# ./mmseqs_clusters.py [mmseqs output] firmicutes_table_1e-70-80_with_seq_v7.csv [file cre
ated by: cat [mmseqs output]| cut -f1| uniq -c| sort -n > output.txt]
# Usage Example:
# ./mmseqs_clusters.py ./approach_1/DB_cl3f_cluster.tsv firmicutes_table_1e-70-80_with_seq
_v7.csv cl3f_clusters.txt
# tsv_cluster_parser.py being this code
# DB_cl3f_cluster.tsv the output from mmseqs easy-clust/linclust
# firmicutes_table_1e-70-80_with_seq_v7.csv the original input data
# cl3f_clusters.txt a file created by cat [mmseqs output]| cut -f1| uniq -c| sort -n > cl3
f_clusters.txt
#%%
import sys
import re
inFile = sys.argv[1]
infile= sys.argv[2]
newFile=sys.argv[3]
#outfile=sys.argv[3]
list=[]
lets_go={}
count={}
how={}
Total=0
with open(inFile, 'r',  encoding='cp1252') as text:
#
for line in text:
    first=line.rsplit("\t")[0]
    if first not in list:
        list.append(first)
    else:
        pass
for item in list: #This list have 361 items
    a1=item.split("_",4)[0:2]
    b1=item.split("_")[2:4]
    a='_'.join(a1)
    b='_'.join(b1)
       lets_go[a+"_"+b]="None"
    #It creates the 361 entries [len(lets_go) its 361]
    with open(infile, 'r',  encoding='cp1252') as doc2:
        for lina in doc2:
    #Here only checks the whole document once
            if a and b in lina:
                lets_go[a+"_"+b]=lina.rsplit("\t")[2]
#with open(outfile, "w") as out1:
for key, value in lets_go.items():
#
 print(key, ' -> ', value)
with open(newFile, 'r',  encoding='cp1252') as i3:
    for lino in i3:
        if key in lino:
            if value in count:
                count[value]+=int(lino.split()[0])
                how[value]+=1
            else:
                count[value]=int(lino.split()[0])
                how[value]=1
               # print (value + ":" + lino.split()[0])
for key, value in count.items():
        print(key,":", value," in ",how[key],"clusters")
        Total+=how[key]
print("Total Clusters:",Total)
