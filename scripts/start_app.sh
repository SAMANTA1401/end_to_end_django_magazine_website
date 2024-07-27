#!/usr/bin/bash 

sed -i 's/\[]/\["43.205.142.12"]/' /home/ubuntu/project_anneshon/projectpk/settings.py

 
python manage.py makemigrations
python manage.py migrate     
# python manage.py collectstatic
# python manage.py runserver
sudo service gunicorn restart
sudo service nginx restart
sudo ufw allow 'Nginx Full'
echo "start app"
#sudo tail -f /var/log/nginx/error.log
#sudo systemctl reload nginx
#sudo tail -f /var/log/nginx/error.log
#sudo nginx -t
#sudo systemctl restart gunicorn
#sudo systemctl status gunicorn
#sudo systemctl status nginx
# Check the status
#systemctl status gunicorn
# Restart:
#systemctl restart gunicorn
#sudo systemctl status nginx