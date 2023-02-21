# Generated by Django 4.1.5 on 2023-02-21 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField(blank=True)),
                ('job_title', models.TextField(blank=True)),
                ('date_applied', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('method_of_applications', models.TextField(blank=True)),
                ('referrals', models.TextField(blank=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
