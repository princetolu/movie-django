# Generated by Django 4.2 on 2023-06-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_post_mins_post_rating_post_year_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="cover",
            field=models.ImageField(default="", upload_to="images"),
        ),
    ]
