# Generated by Django 5.0.1 on 2024-01-13 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_resumecategory_remove_resume_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='frontend.resumecategory', verbose_name='Category'),
            preserve_default=False,
        ),
    ]