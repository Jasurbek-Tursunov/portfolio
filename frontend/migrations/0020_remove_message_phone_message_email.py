# Generated by Django 5.0.1 on 2024-01-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0019_info_location_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='phone',
        ),
        migrations.AddField(
            model_name='message',
            name='email',
            field=models.EmailField(default='a@gmail.com', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
