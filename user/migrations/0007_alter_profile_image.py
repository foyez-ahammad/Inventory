# Generated by Django 4.0.5 on 2022-07-28 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_profile_image_url_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='static/img/profile/profile.jpg', upload_to=''),
        ),
    ]
