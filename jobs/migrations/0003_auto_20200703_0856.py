# Generated by Django 3.0.8 on 2020-07-03 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200703_0854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='imagefun',
            new_name='image',
        ),
    ]
