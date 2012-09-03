# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('dashboard_userprofile')


    def backwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('dashboard_userprofile', (
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('dashboard', ['UserProfile'])


    models = {
        
    }

    complete_apps = ['dashboard']