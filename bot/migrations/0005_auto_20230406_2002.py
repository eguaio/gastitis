# Generated by Django 2.2.13 on 2023-04-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20230406_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramgroup',
            name='chat_id',
            field=models.BigIntegerField(),
        ),
    ]
