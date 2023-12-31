# Generated by Django 4.2.7 on 2023-11-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="user",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
