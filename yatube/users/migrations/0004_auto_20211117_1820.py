# Generated by Django 2.2.16 on 2021-11-17 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211117_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='photo',
            new_name='avatar',
        ),
    ]
