# Generated by Django 2.2.13 on 2020-06-21 05:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buylist', '0008_product_section'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BuyListItem',
            new_name='Item',
        ),
    ]
