import cobra

model = cobra.io.load_json_model('./inputs/_m_model.json')

model.metabolites.act_c.id = 'actPO4_c'

cobra.io.save_json_model(model,'./inputs/m_model.json')