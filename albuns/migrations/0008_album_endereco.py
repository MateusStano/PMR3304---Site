# Generated by Django 4.1.1 on 2022-12-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albuns', '0007_album_especialidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='endereco',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
