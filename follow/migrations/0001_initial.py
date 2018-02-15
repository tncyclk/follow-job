# Generated by Django 2.0.1 on 2018-02-15 13:11

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=120, verbose_name='Konu')),
                ('tracker', models.CharField(choices=[('BUG', 'bug'), ('FEATURE', 'feature'), ('TEST', 'test'), ('RESEARCH', 'research'), ('SUPPORT', 'support')], default='bug', max_length=50, verbose_name='İşin Tipi')),
                ('description', models.TextField(blank=True, verbose_name='Yorum')),
                ('status', models.CharField(choices=[('NEW', 'new'), ('IN PROGRES', 'in progres'), ('TESTING', 'testing'), ('RESOLVED', 'resolved')], default='new', max_length=50, verbose_name='Durum')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Başlangıç Tarihi')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Bitiş Tarihi')),
                ('result', models.TextField(blank=True, verbose_name='Sonuç')),
                ('file', models.FileField(blank=True, upload_to='', verbose_name='Dosya Ekle')),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('assigned_to', models.ManyToManyField(default=None, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Atanan')),
            ],
            options={
                'ordering': ['-start_date', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50, verbose_name='Proje Adı')),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('members', models.ManyToManyField(default=None, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Üyeler')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='project_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='follow.Project'),
        ),
    ]
