# Generated by Django 3.1.7 on 2021-03-10 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapi', '0005_ideasubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='queryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('query', models.CharField(max_length=200)),
            ],
        ),
    ]
