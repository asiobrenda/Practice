# Generated by Django 4.2 on 2024-03-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='topic',
            name='lang_name',
        ),
    ]
