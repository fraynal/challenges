#!/bin/bash

# Setup
target=$(pwd)/slow
rm -rf $target
mkdir $target
cd $target

final_path=""
for letter in {a..t}; do
    # Path is max 4096 long, each letter takes 2 so 2000 deep
    path=$(printf "$letter/%.0s" {1..2000})
    mkdir -p "$path"
    # Create link back
    ln -s $(pwd) "${path}_"
    # Create link forward
    ln -s "${path}_" "${letter}_"

    final_path="${final_path}${letter}_/"
done

echo "slow/$final_path"

