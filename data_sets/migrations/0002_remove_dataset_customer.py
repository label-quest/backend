# Generated by Django 2.1.4 on 2018-12-13 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_sets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='customer',
        ),
    ]
