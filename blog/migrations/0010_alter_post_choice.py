# Generated by Django 3.2.20 on 2023-10-25 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20231025_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='choice',
            field=models.CharField(blank=True, choices=[('3', '!!!'), ('2', '!!'), ('1', '!')], max_length=50, verbose_name='優先順位は？'),
        ),
    ]
