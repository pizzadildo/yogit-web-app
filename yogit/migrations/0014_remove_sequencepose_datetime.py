# Generated by Django 4.2.1 on 2023-06-10 14:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("yogit", "0013_remove_usersequence_poses"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sequencepose",
            name="datetime",
        ),
    ]
