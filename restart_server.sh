#!/bin/bash

source /root/.bash_profile
ps aux | grep manage.py | grep -v grep | awk '{ print "kill -9", $2 }' | sh
cd /root/image-converter/src
nohup /root/image-converter/src/manage.py runserver_plus --cert-file /etc/letsencrypt/live/doctor-robo.com/cert.pem  --key-file /etc/letsencrypt/live/doctor-robo.com/privkey.pem &

