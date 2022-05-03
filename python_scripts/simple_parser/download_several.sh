#!/bin/bash
while IFS= read -r url_and_download_dir
do
  echo "$url_and_download_dir" | python3 download_course.py
done
