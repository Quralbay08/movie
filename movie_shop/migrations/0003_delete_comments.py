# Generated by Django 4.2 on 2024-09-07 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_shop', '0002_alter_category_options_alter_comments_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
