# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20151014_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='person_role',
            new_name='your_role',
        ),
        migrations.AddField(
            model_name='person',
            name='comment',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
