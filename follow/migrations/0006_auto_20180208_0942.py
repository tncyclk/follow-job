# Generated by Django 2.0.2 on 2018-02-08 06:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('follow', '0005_auto_20180208_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='members',
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(default=None, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Üyeler'),
        ),
    ]
