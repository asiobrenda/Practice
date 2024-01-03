# Generated by Django 4.2 on 2023-11-24 20:15

from django.db import migrations, models
import django.db.models.deletion
import practice.apps.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitc2', models.SmallIntegerField(blank=True, default=0)),
                ('description', models.CharField(blank=True, default='', max_length=300)),
            ],
            bases=(models.Model, practice.apps.core.models.ModifyModel),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, default='', max_length=40)),
            ],
            bases=(models.Model, practice.apps.core.models.ModifyModel),
        ),
        migrations.CreateModel(
            name='YearData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.SmallIntegerField(default=0)),
                ('value', models.SmallIntegerField(default=0)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_year_data', to='asio.product')),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_year_data', to='asio.source')),
            ],
            bases=(models.Model, practice.apps.core.models.ModifyModel),
        ),
    ]
