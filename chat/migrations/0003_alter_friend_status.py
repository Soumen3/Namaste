# Generated by Django 5.0.6 on 2024-07-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_friend_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='status',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('blocked', 'Blocked')], default='unknown', max_length=10),
        ),
    ]