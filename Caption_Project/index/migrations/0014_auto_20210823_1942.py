# Generated by Django 3.2.6 on 2021-08-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20210821_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption_1',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption_2',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption_3',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption_4',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption_5',
            field=models.TextField(max_length=30, null=True),
        ),
    ]
