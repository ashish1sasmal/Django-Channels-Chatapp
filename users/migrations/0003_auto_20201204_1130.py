# Generated by Django 3.1.2 on 2020-12-04 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='user1',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='prof1', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='user2',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='prof2', to='users.profile'),
        ),
    ]
