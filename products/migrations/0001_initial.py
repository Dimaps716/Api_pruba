# Generated by Django 3.0.8 on 2020-10-30 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('picture_url', models.URLField()),
                ('url_located', models.URLField()),
                ('category', models.CharField(max_length=80)),
                ('stores', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
                'ordering': ['id'],
            },
        ),
    ]
