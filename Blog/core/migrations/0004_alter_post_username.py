# Generated by Django 5.0.1 on 2024-01-21 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Username',
            field=models.TextField(max_length=100),
        ),
    ]