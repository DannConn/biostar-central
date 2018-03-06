# Generated by Django 2.0.1 on 2018-03-05 17:32

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=32, unique=True)),
                ('name', models.CharField(default='', max_length=80)),
                ('max_upload_size', models.IntegerField(default=0)),
                ('state', models.IntegerField(choices=[(1, 'New'), (2, 'Active'), (3, 'Suspended'), (4, 'Banned')], default=1)),
                ('role', models.IntegerField(choices=[(1, 'Normal User'), (2, 'Moderator')], default=1)),
                ('notify', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
