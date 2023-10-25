# Generated by Django 3.2.20 on 2023-10-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20231022_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='aboutdeadline',
            field=models.DateField(blank=True, null=True, verbose_name='いつまでにやらないといけない？'),
        ),
        migrations.AddField(
            model_name='post',
            name='spendtime',
            field=models.TimeField(blank=True, null=True, verbose_name='どのくらいかかる？'),
        ),
        migrations.AlterField(
            model_name='post',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='いつまでにやらないといけない？'),
        ),
        migrations.AlterField(
            model_name='post',
            name='finish_data',
            field=models.DateTimeField(blank=True, null=True, verbose_name='いつまで？'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_data',
            field=models.DateTimeField(blank=True, null=True, verbose_name='いつから？'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='どんな内容？'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=' ', max_length=10, verbose_name='どんなタスク？'),
        ),
    ]