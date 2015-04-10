# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150410_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservote',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uservote',
            name='voter',
            field=models.ForeignKey(related_name='given_vote', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
