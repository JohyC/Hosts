#!/bin/bash!bash
for Script in *.sh;
  do
    if [[ $Script == $BASH_SOURCE ]];then
      continue;
    fi
    sh "$Script"
done
