# Generated by Django 4.2 on 2024-08-09 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_post_content"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="categoty",
            new_name="category",
        ),
    ]
