# Generated by Django 5.1.1 on 2024-09-16 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unversity', '0003_kafedra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('kafedra', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='unversity.kafedra')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unversity.student')),
            ],
        ),
    ]
