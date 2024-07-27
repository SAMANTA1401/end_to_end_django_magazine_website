#!/usr/bin/env bash

sudo chown -R ubuntu:ubuntu ~/project_anneshon
virtualenv -p python3 /home/ubuntu/project_anneshon/venv
source /home/ubuntu/project_anneshon/venv/bin/activate
echo "activated venv"
pip3 install -r /home/ubuntu/project_anneshon/requirements.txt
echo "installed req.txt"
