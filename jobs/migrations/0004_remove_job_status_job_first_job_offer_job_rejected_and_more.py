# Generated by Django 4.1.5 on 2023-02-22 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='status',
        ),
        migrations.AddField(
            model_name='job',
            name='first',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='second',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='third',
            field=models.BooleanField(default=False),
        ),
    ]
