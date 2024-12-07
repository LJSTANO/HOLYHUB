# Generated by Django 5.1.2 on 2024-12-03 10:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0009_remove_member_password1_remove_member_password2'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.RemoveField(
            model_name='member',
            name='username',
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
