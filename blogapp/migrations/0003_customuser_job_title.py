# Generated by Django 5.2.3 on 2025-07-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='job_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
