#!/bin/bash
while IFS= read -r url_and_download_dir
do
  IFS=' '
  read -ra directory <<< "$url_and_download_dir"
  if [ ! -d "${directory[1]}" ]
  then
    mkdir "${directory[1]}"
  fi
  echo "$url_and_download_dir" | python3 download_course.py
done
