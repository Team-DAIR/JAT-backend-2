# Generated by Django 4.1.5 on 2023-02-22 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('pending', 'Pending'), ('rejected', 'Rejected')], max_length=10),
        ),
    ]
