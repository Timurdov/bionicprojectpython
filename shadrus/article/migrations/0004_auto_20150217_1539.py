# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comments_comments_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_from',
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
