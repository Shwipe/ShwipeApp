# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shwipe', '0002_auto_20151107_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shwiper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='shwiped',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shwiper',
            name='product',
            field=models.ForeignKey(to='shwipe.Product'),
        ),
        migrations.AddField(
            model_name='shwiper',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
