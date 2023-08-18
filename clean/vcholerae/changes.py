import cobra

model = cobra.io.read_sbml_model('./inputs/m_model.xml')

## Modify IDs for consistency with genbank
for r in model.reactions:
    if r.gene_reaction_rule:
        if 'VC' in r.gene_reaction_rule:
            r.gene_reaction_rule = r.gene_reaction_rule.replace('VC','VC_')
            r.update_genes_from_gpr()
## Trim old genes
cobra.manipulation.remove_genes(model, [g for g in model.genes if not g.reactions])

## Change compartment convention
for m in model.metabolites:
    root = m.id.split('[')[0]
    compartment = m.id[-2]
    new_id = root + '_' + compartment
    m.id = new_id

## Change amino acid convention
for m in model.metabolites:
    if '-L_' in m.id:
        m.id = m.id.replace('-L_','__L_')
##
cobra.io.save_json_model(model,'./inputs/m_model.json')


##
import pandas as pd