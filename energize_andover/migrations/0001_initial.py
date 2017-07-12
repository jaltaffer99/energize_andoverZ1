# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-10 16:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Number', models.CharField(default='0', max_length=10)),
                ('FQN', models.CharField(default='MWSB', max_length=50)),
                ('Function', models.CharField(default='NA', max_length=50)),
                ('Notes', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Closet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Old_Name', models.CharField(default='', max_length=20)),
                ('Notes', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Power', models.CharField(max_length=10)),
                ('Location', models.CharField(max_length=30)),
                ('Number', models.IntegerField(default=0)),
                ('Notes', models.CharField(default='', max_length=1000)),
                ('Associated_Device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='energize_andover.Device')),
                ('Circuit', models.ManyToManyField(blank=True, to='energize_andover.Circuit')),
            ],
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Voltage', models.CharField(default='0', max_length=20)),
                ('Location', models.CharField(default='', max_length=30)),
                ('FQN', models.CharField(default='MWSB', max_length=50)),
                ('Notes', models.CharField(default='', max_length=1000)),
                ('Closet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='energize_andover.Closet')),
                ('Panels', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='energize_andover.Panel')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('OldName', models.CharField(default='', max_length=30)),
                ('Type', models.CharField(default='', max_length=30)),
                ('Notes', models.CharField(default='', max_length=1000)),
                ('Panels', models.ManyToManyField(blank=True, to='energize_andover.Panel')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notes', models.CharField(default='', max_length=1000)),
                ('Authorized_Schools', models.ManyToManyField(blank=True, to='energize_andover.School')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transformer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Notes', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='School',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='energize_andover.School'),
        ),
        migrations.AddField(
            model_name='panel',
            name='School',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='energize_andover.School'),
        ),
        migrations.AddField(
            model_name='device',
            name='Room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='energize_andover.Room'),
        ),
        migrations.AddField(
            model_name='device',
            name='School',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='energize_andover.School'),
        ),
        migrations.AddField(
            model_name='closet',
            name='School',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='energize_andover.School'),
        ),
        migrations.AddField(
            model_name='circuit',
            name='Panel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='energize_andover.Panel'),
        ),
        migrations.AddField(
            model_name='circuit',
            name='Rooms',
            field=models.ManyToManyField(blank=True, to='energize_andover.Room'),
        ),
        migrations.AddField(
            model_name='circuit',
            name='School',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='energize_andover.School'),
        ),
    ]
