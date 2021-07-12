# Generated by Django 3.2.5 on 2021-07-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField()),
                ('status_input1', models.BooleanField()),
                ('status_input2', models.BooleanField()),
                ('status_output1', models.BooleanField()),
                ('status_output2', models.BooleanField()),
                ('voltage', models.IntegerField()),
                ('temperature', models.IntegerField()),
            ],
        ),
    ]