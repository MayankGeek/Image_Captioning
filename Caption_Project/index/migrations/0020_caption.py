# Generated by Django 3.2.6 on 2021-09-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0019_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption1', models.TextField()),
                ('caption2', models.TextField()),
                ('caption3', models.TextField()),
                ('caption4', models.TextField()),
                ('caption5', models.TextField()),
            ],
        ),
    ]
