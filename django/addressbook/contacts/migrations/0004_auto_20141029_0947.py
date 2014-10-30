# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20141029_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='First_name',
            new_name='first_name',
        ),
    ]
