#!/bin/bash

file="$1"
# Check if the file contains "secret"
if [[ "$file" != *"secret"* ]]; then
    # Check if the file is a symlink
    if [ ! -h "$file" ]; then
        # < EXPLOITABLE WINDOW >
        cat "$file"
    else
        echo "Error: File is a symlink."
    fi
else
    echo "Error: File may not contain 'secret'."
fi


