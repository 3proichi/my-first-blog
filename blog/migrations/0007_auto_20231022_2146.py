# Generated by Django 3.2.20 on 2023-10-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20231011_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='finish_data',
            field=models.DateTimeField(blank=True, null=True, verbose_name='終了日時'),
        ),
        migrations.AddField(
            model_name='post',
            name='start_data',
            field=models.DateTimeField(blank=True, null=True, verbose_name='開始日時'),
        ),
    ]
