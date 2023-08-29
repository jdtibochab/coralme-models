import cobra


model = cobra.io.read_sbml_model('./inputs/m_model.xml')
cobra.io.save_json_model(model,'./inputs/m_model.json')

