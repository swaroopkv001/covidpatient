# Generated by Django 4.0.1 on 2022-02-04 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dr_name', models.CharField(max_length=70)),
                ('Specialization', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital_name', models.CharField(max_length=100)),
                ('Hospital_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('Dr', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calc.doctor')),
                ('hospital', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calc.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RTPCR', models.CharField(max_length=20)),
                ('Rap_antigen', models.CharField(max_length=20)),
                ('patient', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calc.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Condition', models.CharField(max_length=50)),
                ('Discharge_date', models.DateField()),
                ('result', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calc.test')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calc.hospital'),
        ),
        migrations.CreateModel(
            name='Bed_avail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ICU', models.IntegerField()),
                ('Special', models.IntegerField()),
                ('General', models.IntegerField()),
                ('hospital', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calc.hospital')),
            ],
        ),
    ]