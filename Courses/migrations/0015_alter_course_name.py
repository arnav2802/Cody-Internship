# Generated by Django 5.0.6 on 2024-08-31 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0014_alter_cart_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
