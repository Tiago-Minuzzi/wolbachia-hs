#/usr/bin/env python3
import os
import sys

FASTA=sys.argv[1]
fasta_name=os.path.splitext(os.path.basename(FASTA))[0]
fasta_dir=os.path.dirname(FASTA)
OCSV=os.path.join(fasta_dir,f'{fasta_name}.csv')
fas_dict={}
with open(FASTA) as fasta, open(OCSV,'w') as ocsv:
    fasta=fasta.readlines()
    for num, linha in enumerate(fasta):
        linha=linha.strip()
        if linha.startswith('>'):
            fid=linha[1:]
            fas_dict[fid]=''
            num=str(int(num/2))
            num_pad=num.zfill(4)
            indfas=f'fasin_{num_pad}'
            ocsv.write(f'{indfas},{fid}\n')
            print(f'>{indfas}')
        else:
            fas_dict[fid]=linha
            print(linha)
