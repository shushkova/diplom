# Generated by Django 3.0.5 on 2020-04-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0002_auto_20200430_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='external_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='ID пользователя'),
        ),
    ]
