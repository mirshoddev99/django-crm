# Generated by Django 4.1.7 on 2023-02-26 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='state',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='address',
            new_name='country',
        ),
    ]