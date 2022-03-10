#!/usr/bin/env python
# coding: utf-8
import pandas as pd

# ## Supergroup A
sga = pd.read_excel('supplementary_table_2.xlsx',skiprows=1,index_col='wolb')

# sample selection
dana = sga.loc[sga.index.str.contains('Dvir_'),sga.columns.str.contains('Dana_')]
dnov = sga.loc[sga.index.str.contains('Dvir_'),sga.columns.str.contains('Dnov_')]
dmel = sga.loc[sga.index.str.contains('Dvir_'),sga.columns.str.contains('Dmel_')]
dall = sga.loc[sga.index.str.contains('Dvir_'),sga.columns.str.contains('Dall_')]

# #### Dufourea novaeangliae
dnov_descr = dnov.describe().T
dnov_descr_overall = dnov_descr[['mean','std','min','max']].describe().T[['mean','std','min','max']]
dnov_descr_overall.rename(columns={'mean':'overall_mean',
                                   'std':'overall_std',
                                   'min':'overall_min',
                                   'max':'overall_max'},inplace=True)
# save to file
with pd.ExcelWriter('dvir_dnov_all.xlsx') as writer01:
    dnov.to_excel(writer01, sheet_name='dvir_vs_dnov')
    dnov_descr.to_excel(writer01, sheet_name='dvir_vs_dnov_stats')
    dnov_descr_overall.to_excel(writer01, sheet_name='dvir_vs_dnov_overall_stats')

# #### Drosophila melanogaster
dmel_descr = dmel.describe().T
dmel_descr_overall = dmel_descr[['mean','std','min','max']].describe().T[['mean','std','min','max']]
dmel_descr_overall.rename(columns={'mean':'overall_mean',
                                   'std':'overall_std',
                                   'min':'overall_min',
                                   'max':'overall_max'},inplace=True)
# save to file
with pd.ExcelWriter('dvir_dmel_all.xlsx') as writer01:
    dmel.to_excel(writer01, sheet_name='dvir_vs_dmel')
    dmel_descr.to_excel(writer01, sheet_name='dvir_vs_dmel_stats')
    dmel_descr_overall.to_excel(writer01, sheet_name='dvir_vs_dmel_overall_stats')

# #### Drosophila ananassae
dana_descr = dana.describe().T
dana_descr_overall = dana_descr[['mean','std','min','max']].describe().T[['mean','std','min','max']]
dana_descr_overall.rename(columns={'mean':'overall_mean',
                                   'std':'overall_std',
                                   'min':'overall_min',
                                   'max':'overall_max'},inplace=True)
# save to file
with pd.ExcelWriter('dvir_dana_all.xlsx') as writer01:
    dana.to_excel(writer01, sheet_name='dvir_vs_dana')
    dana_descr.to_excel(writer01, sheet_name='dvir_vs_dana_stats')
    dana_descr_overall.to_excel(writer01, sheet_name='dvir_vs_dana_overall_stats')

# #### Diachasma alloeum
dall_descr = dall.describe().T
dall_descr_overall = dall_descr[['mean','std','min','max']].describe().T[['mean','std','min','max']]
dall_descr_overall.rename(columns={'mean':'overall_mean',
                                   'std':'overall_std',
                                   'min':'overall_min',
                                   'max':'overall_max'},inplace=True)
# save to file
with pd.ExcelWriter('dvir_dall_all.xlsx') as writer01:
    dall.to_excel(writer01, sheet_name='dvir_vs_dall')
    dall_descr.to_excel(writer01, sheet_name='dvir_vs_dall_stats')
    dall_descr_overall.to_excel(writer01, sheet_name='dvir_vs_dall_overall_stats')

# ## Supergroup B
sgb = pd.read_excel('supplementary_table_3.xlsx',skiprows=1,index_col='wolb')

# #### Tetranychus urticae
Turt = sgb.loc[sgb.index.str.contains('Dcit_'),sgb.columns.str.contains('Turt_')]
Turt_descr = Turt.describe().T[['mean','std','min','max']]

# #### Drosophila mauritiana
Dmau = sgb.loc[sgb.index.str.contains('Dcit_'),sgb.columns.str.contains('Dmau_')]
Dmau_descr = Dmau.describe().T[['mean','std','min','max']]

# #### Homalodisca vitripennis
Hvit = sgb.loc[sgb.index.str.contains('Dcit_'),sgb.columns.str.contains('Hvit_')]
Hvit_descr = Hvit.describe().T[['mean','std','min','max']]

# #### Aedes albopictus
Aalb = sgb.loc[sgb.index.str.contains('Dcit_'),sgb.columns.str.contains('Aalb_')]
Aalb_descr = Aalb.describe().T[['mean','std','min','max']]

# Concat sgb stats
sgb_sel_stats = pd.concat([Aalb_descr,Dmau_descr,Hvit_descr,Turt_descr])
sgb_sel_stats = sgb_sel_stats.rename_axis(index='wolb')

# Save to xlsx file
with pd.ExcelWriter('sgb_stats_supp.xlsx') as writer02:
    sgb_sel_stats.to_excel(writer02,sheet_name='descriptive_statistics')
    Aalb.to_excel(writer02,sheet_name='dcit_vs_aalb')
    Dmau.to_excel(writer02,sheet_name='dcit_vs_dmau')
    Hvit.to_excel(writer02,sheet_name='dcit_vs_hvit')
    Turt.to_excel(writer02,sheet_name='dcit_vs_turt')