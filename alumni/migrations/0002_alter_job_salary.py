# Generated by Django 4.0.6 on 2022-09-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(help_text='Eg: 230,000', max_length=25),
        ),
    ]
