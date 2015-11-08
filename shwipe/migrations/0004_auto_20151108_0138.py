# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shwipe', '0003_auto_20151108_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shwipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direction', models.CharField(max_length=100, choices=[(b'Left', b'Left'), (b'Right', b'Right')])),
                ('product', models.ForeignKey(to='shwipe.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='shwiper',
            name='product',
        ),
        migrations.RemoveField(
            model_name='shwiper',
            name='user',
        ),
        migrations.DeleteModel(
            name='Shwiper',
        ),
    ]
