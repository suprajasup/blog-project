# Generated by Django 2.1.7 on 2019-02-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='all_covers/cover.png', upload_to='all_covers/'),
        ),
    ]