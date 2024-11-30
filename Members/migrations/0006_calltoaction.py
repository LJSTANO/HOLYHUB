# Generated by Django 5.1.2 on 2024-11-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0005_alter_service_description_alter_service_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the Call to Action section', max_length=255)),
                ('description', models.TextField(help_text='Description or message for the Call to Action')),
                ('button_text', models.CharField(default='Call To Action', help_text='Text for the CTA button', max_length=100)),
            ],
        ),
    ]