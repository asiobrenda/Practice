# Generated by Django 4.2 on 2023-12-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30, null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]