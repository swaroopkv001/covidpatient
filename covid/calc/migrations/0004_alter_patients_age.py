# Generated by Django 4.0.1 on 2022-02-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_alter_patients_address_alter_patients_fname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
