# Generated by Django 2.0.2 on 2018-02-08 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0004_job_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='project_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='follow.Project'),
        ),
    ]
