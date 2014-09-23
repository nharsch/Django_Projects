# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UploadFile'
        db.create_table(u'main_uploadfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['UploadFile'])

        # Adding model 'PackJob'
        db.create_table(u'main_packjob', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prodid', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('asset_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'main', ['PackJob'])

        # Adding model 'BatchJob'
        db.create_table(u'main_batchjob', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal(u'main', ['BatchJob'])

        # Adding M2M table for field job_list on 'BatchJob'
        m2m_table_name = db.shorten_name(u'main_batchjob_job_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('batchjob', models.ForeignKey(orm[u'main.batchjob'], null=False)),
            ('packjob', models.ForeignKey(orm[u'main.packjob'], null=False))
        ))
        db.create_unique(m2m_table_name, ['batchjob_id', 'packjob_id'])


    def backwards(self, orm):
        # Deleting model 'UploadFile'
        db.delete_table(u'main_uploadfile')

        # Deleting model 'PackJob'
        db.delete_table(u'main_packjob')

        # Deleting model 'BatchJob'
        db.delete_table(u'main_batchjob')

        # Removing M2M table for field job_list on 'BatchJob'
        db.delete_table(db.shorten_name(u'main_batchjob_job_list'))


    models = {
        u'main.batchjob': {
            'Meta': {'object_name': 'BatchJob'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.PackJob']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        u'main.packjob': {
            'Meta': {'object_name': 'PackJob'},
            'asset_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'prodid': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'main.uploadfile': {
            'Meta': {'object_name': 'UploadFile'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['main']