# Generated by Django 5.2.1 on 2025-05-24 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_links',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
