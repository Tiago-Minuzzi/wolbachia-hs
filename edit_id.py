#!/usr/bin/env python3
import re
import sys
ARQ=sys.argv[1]
TAB=sys.argv[2]


def read_fasta(ARQ):
    with open(ARQ, 'r') as fasta:
        fasta=fasta.readlines()
        fasdict={}
        for line in fasta:        
            line = line.strip()
            if line.startswith('>'):
                fid=line
                fasdict[fid]=''
            else:
                fasdict[fid] += line
        return fasdict

def read_table(TAB):
    with open(TAB,'r') as tabela:
        wolbs=[]
        for linha in tabela:
            host, wolb, *_ = linha.split(',')
            host=host.replace(' ','-')
            wolbs.append(f'{host},{wolb}')
        return wolbs


tabela = read_table(TAB)
fasta = read_fasta(ARQ)

for k, v in fasta.items():
    for i in tabela:
        h,w = i.split(',')
        if w in k:
            new_id = k.replace('>',f'>{h}.')
            new_id = re.sub('_.*','',new_id)
            print(f'{new_id}\n{v}')
