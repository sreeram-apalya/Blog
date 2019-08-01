# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20190729_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='sta/'),
        ),
    ]
