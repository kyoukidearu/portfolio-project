# Generated by Django 3.0.8 on 2020-07-03 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='image',
            new_name='imagefun',
        ),
    ]
