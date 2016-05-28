# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dosya',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dosya_adi', models.TextField()),
                ('arsa_sahibi', models.TextField()),
                ('yapimci_firma', models.TextField()),
                ('araci_firma', models.TextField()),
                ('ek_notlar', models.TextField()),
                ('il', models.TextField()),
                ('ilce', models.TextField()),
                ('belediye', models.TextField()),
                ('pafta', models.TextField()),
                ('ada', models.TextField()),
                ('parsel', models.TextField()),
                ('kayit_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncelleme_tarihi', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
