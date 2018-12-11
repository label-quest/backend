# Generated by Django 2.1.2 on 2018-12-11 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_sets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(max_length=4096)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_sets.DataSet')),
            ],
        ),
    ]
