# Generated by Django 4.1.13 on 2024-03-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_employee_econtact'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='Econtact',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Eid',
            field=models.CharField(max_length=10),
        ),
    ]