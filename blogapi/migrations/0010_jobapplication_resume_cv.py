# Generated by Django 3.1.7 on 2021-03-11 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapi', '0009_remove_jobapplication_resume_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='resume_cv',
            field=models.FileField(default='', upload_to='media/'),
        ),
    ]
