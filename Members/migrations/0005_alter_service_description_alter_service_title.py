# Generated by Django 5.1.2 on 2024-11-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0004_service_delete_call'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]