# Generated by Django 2.1.2 on 2018-10-07 09:53

from django.db import migrations, models
import django.db.models.functions.datetime


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.db.models.functions.datetime.Now())),
                ('input_number', models.TextField(max_length=255)),
                ('output_number', models.TextField(max_length=255)),
            ],
        ),
    ]
