# Generated by Django 4.1.3 on 2022-11-06 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albuns', '0002_remove_list_author_list_desc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Provider',
        ),
    ]