# Generated by Django 2.1.4 on 2018-12-17 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('potential_labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potentiallabel',
            name='data_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='potential_labels', to='data_sets.DataSet'),
        ),
    ]
