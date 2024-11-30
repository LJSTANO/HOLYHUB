# Generated by Django 5.1.2 on 2024-11-27 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0006_calltoaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='calltoaction',
            name='link_url',
            field=models.URLField(blank=True, help_text='URL for the CTA button link', null=True),
        ),
    ]