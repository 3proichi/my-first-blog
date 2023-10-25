# Generated by Django 3.2.20 on 2023-10-05 08:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20231004_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='task',
        ),
        migrations.AlterField(
            model_name='post',
            name='deadline',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='期日'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=' ', max_length=10, verbose_name='タスク名'),
        ),
    ]