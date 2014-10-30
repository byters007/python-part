# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20141029_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='first_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='First_name',
            field=models.CharField(default='FR', max_length=255, choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.CharField(default='Male', max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')]),
            preserve_default=True,
        ),
    ]
