# Generated by Django 3.2.9 on 2021-11-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
    ]
