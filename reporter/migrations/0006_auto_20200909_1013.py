# Generated by Django 3.1.1 on 2020-09-09 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0005_auto_20200908_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]