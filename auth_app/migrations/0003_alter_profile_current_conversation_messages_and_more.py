# Generated by Django 4.1.7 on 2023-03-31 22:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_profile_current_conversation_messages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_conversation_messages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='summary_conversation',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]
