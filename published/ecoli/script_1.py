#!/usr/bin/python3
df1 = builder.org.enz_rxn_assoc_df
df1.columns = ['From Builder']
df1['From Builder'] = df1['From Builder'].apply(lambda x: ' OR '.join(sorted(x.split(' OR '))))

df2 = builder.df_enz2rxn
df2.columns = ['From OSM']
df2['From OSM'] = df2['From OSM'].apply(lambda x: ' OR '.join(sorted(x.split(' OR '))))

df3 = pandas.concat([df1, df2], axis = 1)
df3[df3['From Builder'] != df3['From OSM']].to_csv('Wrong_Enz2Reactions.txt', sep = '\t')
