# Generated by Django 2.2 on 2019-04-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=90)),
                ('category', models.CharField(choices=[('desarrollo', 'desarrollo'), ('comunidad', 'comunidad')], max_length=30)),
                ('date_init', models.DateField()),
                ('date_finish', models.DateField()),
                ('state', models.CharField(choices=[('ejecucion', 'ejecucion'), ('terminacion', 'terminacion')], max_length=30)),
            ],
        ),
    ]
