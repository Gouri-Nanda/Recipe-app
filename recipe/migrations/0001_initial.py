# Generated by Django 5.0.2 on 2024-04-18 04:38

import recipe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe_data',
            fields=[
                ('recipe_Id', models.AutoField(primary_key=True, serialize=False)),
                ('recipe_name', models.CharField(max_length=200)),
                ('recipe_desc', models.CharField(max_length=200)),
                ('recipe_para', models.TextField()),
                ('recipe_photo', models.FileField(null=True, upload_to=recipe.models.user_directory_path, verbose_name='')),
            ],
            options={
                'db_table': 'recipe',
            },
        ),
    ]