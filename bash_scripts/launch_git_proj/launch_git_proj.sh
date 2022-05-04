#!/bin/bash
git_projects_path="$HOME/Documents/current_work/programming/git_projects/"
projects_list="$(ls -1 $git_projects_path)"
message_templ=("You have the following programming projects:" $projects_list "")
printf '%s\n' "${message_templ[@]}"
read -p "Which one you want to work work with? Enter the name: " project_name
project_dir="$git_projects_path$project_name"
# new tab with termdown running in counter mode
xfce4-terminal --tab --execute termdown
# connect to github
xfce4-terminal --tab --title=git --working-directory=$project_dir --execute bash -c 'eval $(ssh-agent) -s; ssh-agent -s; ssh-add $HOME/.ssh/git_key; ssh -T git@github.com; exec bash'
# new tab for editing code
xfce4-terminal --tab --title=vim --working-directory=$project_dir
# new tab for testing code
xfce4-terminal --tab --title=tests --working-directory=$project_dir
