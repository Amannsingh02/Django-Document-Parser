# Generated by Django 4.1.3 on 2023-08-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_uploader', '0002_textfile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfile',
            name='filename',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
