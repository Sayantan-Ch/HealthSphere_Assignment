# Generated by Django 4.2.4 on 2023-08-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_alter_doctor_id_alter_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.TextField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]