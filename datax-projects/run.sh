#!/bin/sh
# Add this to /etc/rc.local on a python server.
# cd /path/to/app
# ./start.sh
# nohup python server/main.py > logging.out
open http://127.0.0.1:5000/
python server/main.py > logging.out
