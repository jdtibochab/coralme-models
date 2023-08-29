import pandas as pd

genes = pd.read_csv('./building_data/_genes.txt',sep='\t',index_col=0)
genes.drop('Accession-2',axis=1,inplace=True)
genes.to_csv('./building_data/genes.txt',sep='\t')