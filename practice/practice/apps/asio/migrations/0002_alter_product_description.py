# Generated by Django 4.2 on 2023-11-25 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
