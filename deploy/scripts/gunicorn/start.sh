#!/bin/bash

NAME="twitchscore"
DJANGODIR=/home/asnelzin/twitchscore
DJANGO_SETTINGS_MODULE=twitchscore.settings.production
DJANGO_WSGI_MODULE=twitchscore.wsgi
LOGFILE=/home/asnelzin/twitchscore/logs/gunicorn.log
PIDFILE=/home/asnelzin/twitchscore/pids/gunicorn.pid
NUM_WORKERS=3
USER=asnelzin
GROUP=asnelzin

echo "Starting $NAME as `whoami`"

source /home/asnelzin/.virtualenvs/twitchscore/bin/postactivate
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

exec /home/asnelzin/.virtualenvs/twitchscore/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name=$NAME \
    --workers=$NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --bind=localhost:8001 \
    --log-level=debug \
    --log-file=$LOGFILE \
    --pid=$PIDFILE

