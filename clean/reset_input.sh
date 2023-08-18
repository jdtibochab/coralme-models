for i in $( find . -maxdepth 1 -type d -not -name "." -not -name ".ipynb*")
    do
        base=${i##*/}
        echo "Processing... " $base
        
#         find ./$base/building_data/ -name "*.txt" | xargs rm
        
#         sed -i 's|"fes_transfers" : \[\]|"fes_transfers" : \[\],|g' ./$base/organism.json
        
#         cp ./vcholerae/building_data/subreaction_matrix.txt ./$base/building_data/
        
#         sed -i "s#\"df_metadata_orphan_rxns\": \"\"#\"df_metadata_orphan_rxns\": \"./$base/building_data/orphan_and_spont_reactions.txt\"#g" ./$base/input.json
#         sed -i "s#\"df_metadata_metabolites\": \"\"#\"df_metadata_metabolites\": \"./$base/building_data/me_metabolites.txt\"#g" ./$base/input.json

#         sed -i "s/${base}_clean/$base/g" ./$base/input.json

#         rm ./$base/inputs/subreaction_matrix.txt
#         sed -i "s/${base}_clean/$base/g" ./$base/input.json
#         sed -i "s/${base}_clean/$base/g" ./$base/organism.json

#         cp ../draft_cobrame/draft_cobrame/organisms/$base/building_data/genome.gb ./$base/inputs/
    done