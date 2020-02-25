#!/bin/bash

ps aux | grep manage.py | grep -v grep | awk '{ print "kill -9", $2 }' | sh
cd src
nohup ./manage.py runserver_plus --cert-file ./cert.pem  --key-file ./privkey.pem &

