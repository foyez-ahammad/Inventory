# Generated by Django 4.0.5 on 2022-07-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_url',
            field=models.CharField(default='https://source.unsplash.com/640x950/?profile', max_length=3000),
        ),
    ]