# Generated by Django 3.2.15 on 2022-11-28 17:24

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='default', max_length=255, validators=[django.contrib.auth.validators.ASCIIUsernameValidator]),
        ),
    ]