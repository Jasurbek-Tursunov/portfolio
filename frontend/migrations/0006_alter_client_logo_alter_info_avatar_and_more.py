# Generated by Django 5.0.1 on 2024-01-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_alter_info_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='logo',
            field=models.ImageField(upload_to='./logos', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='info',
            name='avatar',
            field=models.ImageField(upload_to='./avatars', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='./images', verbose_name='Image'),
        ),
    ]
