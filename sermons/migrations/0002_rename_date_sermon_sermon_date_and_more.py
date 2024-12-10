# Generated by Django 5.1.2 on 2024-12-09 19:37

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sermons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='sermon',
            old_name='date',
            new_name='sermon_date',
        ),
        migrations.RenameField(
            model_name='sermon',
            old_name='preacher',
            new_name='speaker',
        ),
        migrations.RenameField(
            model_name='sermon',
            old_name='youtube_link',
            new_name='youtube_url',
        ),
        migrations.RemoveField(
            model_name='dailydevotion',
            name='scripture',
        ),
        migrations.RemoveField(
            model_name='prayerrequest',
            name='email',
        ),
        migrations.RemoveField(
            model_name='prayerrequest',
            name='name',
        ),
        migrations.RemoveField(
            model_name='prayerrequest',
            name='submitted_at',
        ),
        migrations.RemoveField(
            model_name='prayerrequest',
            name='topic',
        ),
        migrations.AddField(
            model_name='prayerrequest',
            name='date_submitted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='prayerrequest',
            name='is_responded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='prayerrequest',
            name='response',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prayerrequest',
            name='title',
            field=models.CharField(default='Prayer for family', max_length=200),
        ),
        migrations.AddField(
            model_name='prayerrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dailydevotion',
            name='date',
            field=models.DateField(),
        ),
    ]
