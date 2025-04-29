#!/bin/bash
# Empty the final_output.txt file before starting
> diff_report.txt
# For loop through all "out.txt" files that changed in git status
for i in $(git status | grep "out.txt" | awk '{print $2}')
do
    # Print the base name
    echo "Processing... " $i
    
    # Get relevant differences in files
    echo "====================>" $i >> final_output.txt  >> diff_report.txt
    git diff $i | grep -e "Troubleshooter" -e "Gapfilled" >> diff_report.txt
done