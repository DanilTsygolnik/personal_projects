#!/bin/bash

urls="/dev/stdin"
while IFS= read -r line
do
  #echo "$line"
  echo "$line" | python3 html_parser.py
  sleep 5s
done
