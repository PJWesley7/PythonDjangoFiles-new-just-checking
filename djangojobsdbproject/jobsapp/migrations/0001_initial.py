# Generated by Django 5.0.1 on 2024-01-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruiter_name', models.CharField(max_length=255)),
                ('job_id', models.CharField(max_length=255)),
            ],
        ),
    ]