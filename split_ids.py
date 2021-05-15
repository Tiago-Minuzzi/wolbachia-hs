#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:20:51 2021
@author: Tiago Minuzzi

Unpack joined fasta IDs

"""
import sys

# Input and output files
FASTA=sys.argv[1]
UNFASTA=sys.argv[2]
# Individual IDs list and fasta dictionary
lids=[]
fas_dict={}

# Get IDs individually
with open(FASTA) as fasta:
    fasta=fasta.readlines()
    for line in fasta:
        line=line.strip()
        if line.startswith('>'):
            faid=line[1:]
            fas_dict[faid]='' # complete line to dict
            fid=line[1:].split('|') # split id
            if 'revcompl' in fid:
                fid.remove('revcompl')
            for item in fid:
                lids.append(item)
        else:
            fas_dict[faid]=line
            
with open(UNFASTA, 'w') as unfasta:
    for key, value in fas_dict.items():
        for lid in lids:
            if lid in key:
                unfasta.write(f'>{lid}\n{value}\n')
