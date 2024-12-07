# Generated by Django 5.1.2 on 2024-12-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0010_remove_member_email_remove_member_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='image',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default='default@holyhub.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default='holyhub', max_length=128),
        ),
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(default='john', max_length=100, unique=True),
        ),
    ]
