# Generated by Django 4.2 on 2023-06-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0009_post_date_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date_time",
            field=models.DateTimeField(),
        ),
    ]