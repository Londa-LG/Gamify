# Generated by Django 3.0.8 on 2020-08-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='body_challenge_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='status',
            name='mind_challenge_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='status',
            name='skill_challenge_status',
            field=models.BooleanField(default=True),
        ),
    ]
