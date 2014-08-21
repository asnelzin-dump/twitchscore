# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('accounts_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, db_index=True, max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('summoner_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('summoner_id', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('accounts', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('accounts_user')


    models = {
        'accounts.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'summoner_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'summoner_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['accounts']