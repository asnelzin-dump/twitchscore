#!/bin/bash
set -e
DJANGODIR=/home/asnelzin/twitchscore
DJANGO_SETTINGS_MODULE=twitchscore.settings.production

LOGFILE=/home/asnelzin/twitchscore/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
PIDFILE=/home/asnelzin/twitchscore/pids/gunicorn.pid
NUM_WORKERS=3
# user/group to run as
USER=asnelzin
GROUP=asnelzin
cd /home/asnelzin/twitchscore
source /home/asnelzin/.virtualenvs/twitchscore/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

exec /home/asnelzin/.virtualenvs/twitchscore/bin/python /home/asnelzin/twitchscore/manage.py \
  run_gunicorn --workers=$NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug --pid=$PIDFILE \
  --log-file=$LOGFILE --bind=localhost:8001