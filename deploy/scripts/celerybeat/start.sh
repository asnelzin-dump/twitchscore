#!/bin/bash

source /home/asnelzin/.virtualenvs/twitchscore/bin/postactivate
exec /home/asnelzin/.virtualenvs/twitchscore/bin/python \
    /home/asnelzin/twitchscore/manage.py celeryd --beat
