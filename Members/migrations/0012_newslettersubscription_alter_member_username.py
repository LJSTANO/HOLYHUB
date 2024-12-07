# Generated by Django 5.1.2 on 2024-12-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0011_remove_member_image_remove_member_user_member_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(default='Stanley', max_length=100, unique=True),
        ),
    ]
