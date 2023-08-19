This is a repository containing all ME-models reconstructed using `coralME`_.

Description
-----------
Automatically reconstructed ME-models (dME-models) are available in clean/, and updated ME-models (uME-models) are available in published/. We here provide JSON files for minimal (step1), fully reconstructed (step2) and troubleshot (step3) ME-models. For uME-models, step2 and step3 are the same model, just that step3 will have a solution property.

Code to reproduce Figures of our manuscript and to reconstruct ME-models are provided here as python scripts and Jupyter notebooks.

Reconstructing ME-models from Notebooks
---------------------------------------
1. Go to the desired directory, clean/ or published/.
2. Open Supplementary Notebook and follow instructions.

Reconstructing ME-models from command line
------------------------------------------
1. Go to the desired directory, clean/ or published/.
2. run ``bash build.sh 0 1 1 1 ORGANISM_NAME``.

ORGANISM_NAME must exist in directory. The four numbers are binary flags to run (if 1) / not run (if 0): (1) BLASTp, (2) Data synchronization and complementation, (3) ME-model reconstruction and OSM generation, (4) ME-model troubleshooting. Since we provide here BLASTp results, the first number can be set to 0. Setting it to 1 will run a BLASTp with 4 CPU cores and overwrite files in blast_files_and_results under each organisms directory.

Reconstructing all ME-models in directory (parallelized)
--------------------------------------------------------
1. Go to the desired directory, clean/ or published/.
2. run ``bash parallel.sh 0 1 1 1``. The four numbers represent the same flags as described before. **Modify N in parallel.sh to set number of cores, default 4**.

Loading provided ME-models from JSON files
------------------------------------------
In order to inspect, read, and manipulate JSON ME-model files, first extract the compressed .json.gz files.
1. run ``gzip -d ORGANISM_MEMODEL_FILE.json.gz``
2. In a python environment, run ``model = coralme.io.json.load_json_me_model("PATH_TO_MEMODEL_FILE.json")``

.. refs
.. _coralME: https://github.com/jdtibochab/coralme
