# Generated by Django 3.0.4 on 2020-03-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactForm',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
