import cobra

# Previous name interfered with Gurobi (St)
model = cobra.io.load_json_model('./inputs/iLJ478.json')
old_rxn = model.reactions.St
rxn = cobra.Reaction('SULFURt')
model.add_reactions([rxn])
for k,v in old_rxn.metabolites.items():
    rxn.add_metabolites({k.id:v})
rxn.bounds = old_rxn.bounds
rxn.name = old_rxn.name
rxn.subsystem = old_rxn.subsystem
rxn.notes = old_rxn.notes
model.remove_reactions([old_rxn])


# Asparagine not in model, but there is tRNA-Asn, so it should be included
met = cobra.Metabolite('asn__L_c')
met.name = 'L-Asparagine'
met.formula = 'C4H8N2O3'
met.compartment = 'c'
model.add_metabolites([met])

cobra.io.save_json_model(model,'./inputs/m_model.json')

#sed -i 's/TM_1837/TM1837/g' ./inputs/m_model.json