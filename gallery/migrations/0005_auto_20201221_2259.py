# Generated by Django 3.1.3 on 2020-12-21 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20201221_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='uploaded_at',
            new_name='created_at',
        ),
    ]
