# Generated by Django 2.2 on 2019-04-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190411_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
    ]
