# Generated by Django 5.0.6 on 2024-07-17 09:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('blocked', 'Blocked')], default='pending', max_length=10)),
                ('user_1', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='friend_set_1', to=settings.AUTH_USER_MODEL)),
                ('user_2', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='friend_set_2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [models.Index(fields=['user_1'], name='chat_friend_user_1__41083c_idx'), models.Index(fields=['user_2'], name='chat_friend_user_2__56b981_idx')],
                'unique_together': {('user_1', 'user_2')},
            },
        ),
    ]
