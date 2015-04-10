# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote', models.BooleanField(default=False)),
                ('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
                ('voter', models.ForeignKey(related_name='voter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='uservote',
            unique_together=set([('user', 'voter')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
