# Generated by Django 3.1.3 on 2020-11-17 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0002_auto_20201117_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pics',
            old_name='image',
            new_name='images',
        ),
    ]
