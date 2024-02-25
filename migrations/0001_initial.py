# Generated by Django 5.0.2 on 2024-02-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataMonitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinate', models.JSONField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('last_checks', models.DateField()),
                ('analysis_made', models.JSONField()),
            ],
        ),
    ]