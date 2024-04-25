#!/bin/bash

A_Star_tests_states() {
    filename='resultsFile.txt'
    n=0
    dict=()
    while read line; do
    # reading each line
    dict[$n]="korf100/${line:4:6}"
    n=$((n+1))
    done < $filename
    echo ${dict[@]}
}

tests_states="$(A_Star_tests_states)"

test_run(){
    #test_type=$1
    searchFile='Heuristic_Calc.py'
    for kfile in $tests_states; do
    inputFileName="$kfile"
    echo $inputFileName
    python3 $searchFile -f $inputFileName
    echo
    echo "Done"
    echo 
    done

}
test_run 