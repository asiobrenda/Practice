# Generated by Django 4.2 on 2023-09-09 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brenda', '0008_alter_skills_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='percentage',
            field=models.PositiveIntegerField(),
        ),
    ]