# Generated by Django 4.2.6 on 2023-10-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='record_text',
            field=models.CharField(max_length=255),
        ),
    ]
