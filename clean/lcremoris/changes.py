import cobra

model = cobra.io.load_json_model('./inputs/_m_model.json')

## Previous lower bound would make model infeasible at low growth rates
model.reactions.get_by_id("EX_arg__L_e").bounds =  (-1000,0)
model.reactions.get_by_id("EX_glc__D_e").bounds =  (-1000,0)
model.reactions.get_by_id("EX_glu__L_e").bounds =  (-1000,0)
model.reactions.get_by_id("EX_ile__L_e").bounds =  (-1000,0)
model.reactions.get_by_id("EX_leu__L_e").bounds =  (-1000,0)
model.reactions.get_by_id("EX_ser__L_e").bounds =  (-1000,0)
model.reactions.get_by_id("EX_thr__L_e").bounds =  (-1000,0)
model.reactions.get_by_id("EX_val__L_e").bounds =  (-1000,0)
model.reactions.get_by_id("EX_ac_e").bounds =  (0,1000)
model.reactions.get_by_id("EX_etoh_e").bounds =  (0,1000)
model.reactions.get_by_id("EX_for_e").bounds =  (0,1000)
model.reactions.get_by_id("EX_lac__L_e").bounds =  (0,1000)
model.reactions.get_by_id("EX_pro__L_e").bounds =  (0,1000)

##
cobra.io.save_json_model(model,'./inputs/m_model.json')
