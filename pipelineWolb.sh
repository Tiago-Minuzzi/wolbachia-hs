#!/usr/bin/env bash

runSim(){
    INF=$1
    STEM=$(basename $INF .fasta)
    CIAlign --infile $INF --make_similarity_matrix_input --make_simmatrix_keepgaps 2 --plot_input --outfile_stem $STEM 
}

defMen(){
    MSG=$1
    echo ""
    echo $MSG
}

FEXT="*.fasta"
FCAT="concatall.fasta"
FUNQ="uniq_${FCAT}"
INDAT="gpb/$FEXT"
WBREF="host_wolb_info.csv"

SEDID="python3 edit_id.py"
SMACSE="$HOME/sftw/macse/macse_v2.05.jar"
SUNIK="python3 unique_seqs.py"
SSPLIT="split_ids.py"
CONCAT="perl $HOME/sftw/catfasta2phyml/catfasta2phyml.pl -c -f"

DEDIT="01_edid"
DAAA="02_aligned/aa"
DANT="02_aligned/nt"
DCAT="03_concatall"
DUNIQ="04_uniq"
DSIM="05_similarity"

# Edit IDs for host information
mkdir -p $DEDIT
defMen "# Running ID editing..."
    for FILE in $INDAT
    do
        echo "    -$FILE"
        NFILE=${FILE##*\/}
        $SEDID $FILE $WBREF > "$DEDIT"/edid_"$NFILE"
    done &&
defMen "ID editing done!" &&

# Macse alignment
mkdir -p "$DAAA" "$DANT"
defMen "# Running macse alignment..."
    for FILE in $DEDIT/$FEXT
    do
        NFILE=${FILE##*\/}
        java -jar $SMACSE -prog alignSequences -seq $FILE &&
        mv "$DEDIT"/*NT* "$DANT"/${NFILE/edid/align}
        mv "$DEDIT"/*AA* "$DAAA"/${NFILE/edid/align}
    done &&
defMen "Alignment done!" &&

# Concat genes with same ID
mkdir -p $DCAT
defMen "# Running sequence concatenation..."
    sed -i "s/\!/-/g" $DANT/$FEXT
    $CONCAT $DANT/$FEXT > $DCAT/$FCAT &&
defMen "Uniq sequences done!" &&

# Remove redundat sequences
mkdir -p $DUNIQ
defMen "# Removing redundant sequences..."
    $SUNIK $DCAT/$FCAT > $DUNIQ/$FUNQ &&
defMen "Done!" &&

# Similarity analysis
mkdir -p $DSIM
defMen "# Running similarity analysis..."
    runSim "$DUNIQ/$FUNQ" && mv $(basename $FUNQ .fasta)* $DSIM &&
defMen "DONE!"
