# Generated by Django 3.0 on 2020-12-01 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='toUser',
            new_name='toGroup',
        ),
    ]