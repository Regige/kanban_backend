# Generated by Django 4.2.14 on 2024-07-22 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_board', '0002_rename_headline_taskitem_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]