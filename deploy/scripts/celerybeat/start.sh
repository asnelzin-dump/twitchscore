#!/bin/bash

NAME="twitchscore celerybeat"
DJANGODIR=/home/asnelzin/twitchscore

echo "Starting $NAME as `whoami`"

source /home/asnelzin/.virtualenvs/twitchscore/bin/postactivate
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

exec /home/asnelzin/.virtualenvs/twitchscore/bin/python \
    /home/asnelzin/twitchscore/manage.py celerybeat
