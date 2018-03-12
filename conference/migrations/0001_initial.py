# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 07:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reports_name', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('reports_name',),
            },
        ),
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speakers_name', models.CharField(max_length=200)),
                ('about_speakers', models.TextField()),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.AddField(
            model_name='reports',
            name='speakers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speakers', to='conference.Speakers'),
        ),
    ]