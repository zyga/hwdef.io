# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hardware'
        db.create_table(u'hwdef_hardware', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'hwdef', ['Hardware'])


    def backwards(self, orm):
        # Deleting model 'Hardware'
        db.delete_table(u'hwdef_hardware')


    models = {
        u'hwdef.hardware': {
            'Meta': {'object_name': 'Hardware'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['hwdef']