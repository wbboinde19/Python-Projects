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
    test_type=$1
    searchFile='./15md_solver'
    for kfile in $tests_states; do
    inputFileName="$kfile"
    echo >> heavy_cost_results.txt
    echo $inputFileName >> heavy_cost_results.txt
    echo >>heavy_cost_results.txt
    $searchFile astar -cost heavy < $inputFileName >> heavy_cost_results.txt
    echo
    echo "Done"
    echo 
    done

}
test_run "a_star"