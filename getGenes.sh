#!/usr/bin/env bash

geneConcat(){
    GENES=$(cut -f2 $1)
    MONTAGENS=$2
    DIRETORIO=$3

    mkdir -p $DIRETORIO
    echo "Running analysis for $DIRETORIO..."
    for GENE in $GENES
    do
        cat $(find busco_wolbs/WOLB*/run_rickettsiales_odb10/busco_sequences/single_copy_busco_sequences/ -type f -name "$GENE" | grep -f "$MONTAGENS") >> "$DIRETORIO"/gpAB_all_"${GENE/fna/fasta}" && echo "    -${GENE%.fna} files concatenation done."
    done && echo "$DIRETORIO done!" && echo ""
}

geneConcat "new_gpB_top50_gene_list.txt" "wolb_gb_assemb_ids.txt" "new_top_genes/gpb"
