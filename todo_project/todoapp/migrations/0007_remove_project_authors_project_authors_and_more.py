# Generated by Django 4.0.3 on 2022-04-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0009_remove_author_is_staff'),
        ('todoapp', '0006_alter_todo_is_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='authors',
        ),
        migrations.AddField(
            model_name='project',
            name='authors',
            field=models.ManyToManyField(to='authors.author'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_created',
            field=models.DateField(default='2022-04-16'),
        ),
    ]
