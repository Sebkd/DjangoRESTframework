# Generated by Django 4.0.2 on 2022-04-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_rename_user_ptk_author_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=64),
        ),
    ]
