# Generated by Django 4.1.1 on 2022-10-10 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myBlog", "0003_alter_post_create_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="create_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
