# Generated by Django 2.1.7 on 2019-04-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0007_auto_20190402_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('u', 'usd'), ('y', 'yen')], max_length=1)),
                ('rate', models.DecimalField(decimal_places=4, max_digits=10)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='original_amount',
            field=models.DecimalField(decimal_places=2, max_digits=256, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='original_currency',
            field=models.CharField(choices=[('u', 'usd'), ('y', 'yen')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(),
        ),
    ]
