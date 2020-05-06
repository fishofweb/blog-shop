# Generated by Django 3.0.4 on 2020-03-15 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_blog', '0005_auto_20200316_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='back',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('heading1', models.CharField(max_length=50)),
                ('image1', models.ImageField(default='', upload_to='blog/images')),
                ('content1', models.TextField(default='')),
                ('heading2', models.CharField(max_length=50)),
                ('image2', models.ImageField(default='', upload_to='blog/images')),
                ('content2', models.TextField(default='')),
                ('heading3', models.CharField(max_length=50)),
                ('image3', models.ImageField(default='', upload_to='blog/images')),
                ('content3', models.TextField(default='')),
                ('heading4', models.CharField(max_length=50)),
                ('image4', models.ImageField(default='', upload_to='blog/images')),
                ('content4', models.TextField(default='')),
                ('heading5', models.CharField(max_length=50)),
                ('image5', models.ImageField(default='', upload_to='blog/images')),
                ('content5', models.TextField(default='')),
                ('heading6', models.CharField(max_length=50)),
                ('image6', models.ImageField(default='', upload_to='blog/images')),
                ('content6', models.TextField(default='')),
            ],
        ),
    ]
