# Generated by Django 5.0.6 on 2024-07-09 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0006_alter_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='is_preview',
            field=models.BooleanField(default=False),
        ),
    ]
