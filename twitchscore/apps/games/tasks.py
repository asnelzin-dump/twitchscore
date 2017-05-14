from celery import task

from django.core import management


@task
def update_games():
    management.call_command('update_games')
