# Generated by Django 4.2 on 2024-02-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0003_tab_saved_btn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab',
            name='saved_btn',
            field=models.JSONField(null=True),
        ),
    ]
