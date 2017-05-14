import psycopg2
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        conn = psycopg2.connect('db_name=dump_db username=postgres')
        cur = conn.cursor()
        summoners_data = cur.execute('select * from accounts_user;').fetchall()

        for summoner in summoners_data
