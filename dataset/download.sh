#!/bin/bash
current_dir=$(basename "$(pwd)")

if [ "$current_dir" != "dataset" ]; then
    echo "ERROR Current directory is not dataset"
fi

wget https://files.grouplens.org/datasets/movielens/ml-25m.zip
unzip ml-25m.zip