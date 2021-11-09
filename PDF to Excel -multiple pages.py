import tabula
import pandas as pd
dfs = tabula.read_pdf(#enter name of file you want to convert with .pdf extension
"sp.pdf", pages='all', multiple_tables=False,lattice=True)
result_dfs=pd.concat(dfs)
result_dfs.to_excel('VBN.xlsx')
