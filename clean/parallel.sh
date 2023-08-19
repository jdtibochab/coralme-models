task(){
#     sleep 0.5; echo "$1 $2 $3 $4 $5/out.txt";
    echo "Processing... " $5
    python ./build.py ${5#"./"} -bbh $1 -g $2 -b $3 -ts $4 > $5/out.txt 2>&1
}

# initialize a semaphore with a given number of tokens
open_sem(){
    mkfifo pipe-$$
    exec 3<>pipe-$$
    rm pipe-$$
    local i=$1
    for((;i>0;i--)); do
        printf %s 000 >&3
    done
}

# run the given command asynchronously and pop/push tokens
run_with_lock(){
    local x
    # this read waits until there is something to read
    read -u 3 -n 3 x && ((0==x)) || exit $x
    (
     ( "$@"; )
    # push the return code of the command to the semaphore
    printf '%.3d' $? >&3
    )&
}

N=4
open_sem $N
for org in $( find . -maxdepth 1 -type d -not -name "." -not -name ".ipynb*" -not -name "__pycache__" ); do
    run_with_lock task $1 $2 $3 $4 $org
done 