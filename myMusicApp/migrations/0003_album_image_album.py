# Generated by Django 4.1.1 on 2022-10-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myMusicApp", "0002_alter_song_file_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="image_album",
            field=models.ImageField(blank=True, null=True, upload_to="album"),
        ),
    ]
