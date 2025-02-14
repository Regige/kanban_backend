# Generated by Django 4.2.14 on 2024-07-23 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_board', '0006_rename_text_subtaskitem_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSgl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('logogram', models.CharField(max_length=100)),
                ('hex_color', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='taskitem',
            name='assigned_to',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='task_board.contactsgl'),
        ),
    ]
