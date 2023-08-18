import cobra

model = cobra.io.load_json_model('./inputs/_m_model.json')

## Previous lower bound would make model infeasible at low growth rates
model.reactions.get_by_id("EX_fe3_e").bounds = (-67.37,0)
##
cobra.io.save_json_model(model,'./inputs/m_model.json')


##
import pandas as pd