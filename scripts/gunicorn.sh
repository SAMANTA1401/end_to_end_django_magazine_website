#!/usr/bin/bash
sudo cp /home/ubuntu/project_anneshon/gunicorn/gunicorn.socket  /etc/systemd/system/gunicorn.socket
sudo cp /home/ubuntu/project_anneshon/gunicorn/gunicorn.service  /etc/systemd/system/gunicorn.service

sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service
echo "gunicorn start"