# Generated by Django 5.0.6 on 2024-07-24 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0008_usercourse_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
