# Generated by Django 2.0.6 on 2018-07-22 21:09

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0016_postlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestDonations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('expired_at', models.DateTimeField(verbose_name='Дата и время истечение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_request_donations', to='social.Team')),
            ],
            options={
                'verbose_name': 'Запрос на пожертвования',
                'verbose_name_plural': 'Запросы на пожертвования',
            },
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
