# Generated by Django 4.2 on 2023-06-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_post_genere"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="genere",
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
