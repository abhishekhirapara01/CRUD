# Generated by Django 4.1.13 on 2024-04-03 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_company_remove_mobile_company_mobile_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobile',
            old_name='company',
            new_name='company_id',
        ),
    ]