# Generated by Django 5.0.1 on 2024-01-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0021_alter_info_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='birthday',
            field=models.DateField(verbose_name='Birthday'),
        ),
    ]