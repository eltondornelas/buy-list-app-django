# Generated by Django 2.2.13 on 2020-07-03 00:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('buylist', '0010_auto_20200703_0035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['product']},
        ),
    ]
