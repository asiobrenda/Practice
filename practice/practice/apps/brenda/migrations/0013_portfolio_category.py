# Generated by Django 4.2 on 2023-10-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brenda', '0012_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='category',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]