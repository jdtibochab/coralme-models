import os
from coralme.builder.main import MEBuilder
import anyconfig
import sys

def parser(args):
    org = args[1]
    param = {}
    if len(args)>2:
        for idx,a in enumerate(args):
            if '-' not in a: continue
            param[a] = args[idx+1]
    return org,param

def build_model(args):
    org,param = parser(args)
    config = anyconfig.load('{:s}/input.json'.format(org))
    print(config)
    if '-g' not in param or param['-g'] == '1':
        if '-bbh' in param and param['-bbh'] == '0':
            config['run_bbh_blast'] = False
        else:
            config['run_bbh_blast'] = True
        builder = MEBuilder(*['{:s}/organism.json'.format(org)], **config)
        builder.generate_files(overwrite = True)
        builder.save_builder_info()
    else:
        builder = MEBuilder(*['./{:s}/coralme-config.yaml'.format(org)])

    if '-b' not in param or param['-b'] == '1':   
        builder.build_me_model(overwrite = False)
    else:
        builder.me_model = builder.load(builder.configuration['out_directory']+'MEModel-step2-{}.pkl'.format(org))

    if '-ts' not in param or param['-ts'] == '1':   
        builder.troubleshoot(growth_key_and_value = { builder.me_model.mu : config.get("feasibility_mu",0.001) })

build_model(sys.argv)
