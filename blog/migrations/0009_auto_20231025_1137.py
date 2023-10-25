# Generated by Django 3.2.20 on 2023-10-25 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20231022_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='choice',
            field=models.CharField(blank=True, choices=[('3', '!!!'), ('2', '!!'), ('1', '!')], max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='spendtime',
            field=models.FloatField(blank=True, null=True, verbose_name='何時間くらいかかる？'),
        ),
    ]