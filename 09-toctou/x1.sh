#!/bin/sh

while true; do 
    echo 'Hello, world!' > file
    rm file
    ln -s ./secret file
    rm file
done

