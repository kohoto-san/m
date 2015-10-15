# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='company',
            field=models.CharField(default='company', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='fisrt_name',
            field=models.CharField(default='name', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='last name', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='person_role',
            field=models.CharField(default='role', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254),
            preserve_default=True,
        ),
    ]
