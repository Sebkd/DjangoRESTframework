# Generated by Django 4.0.2 on 2022-04-04 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authors', '0005_remove_author_first_name_remove_author_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
