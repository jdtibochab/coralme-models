k=0
for i in $( find . -maxdepth 1 -type d -not -name "." -not -name ".ipynb*" )
    do ((j=j%10)); ((j++==0)) && wait
        echo "Processing... " $i
        python ./build.py ${i#"./"} -bbh $1 -g $2 -b $3 -ts $4 > $i/out.txt 2>&1 &
    done
