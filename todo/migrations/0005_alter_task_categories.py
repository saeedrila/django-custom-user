# Generated by Django 4.1.2 on 2022-10-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_taskcategory_task_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='categories',
            field=models.ManyToManyField(blank=True, to='todo.taskcategory'),
        ),
    ]