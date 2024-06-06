# Generated by Django 5.0.6 on 2024-06-05 07:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stockanalysis", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="news", name="published_date",),
        migrations.AddField(
            model_name="news", name="arrows", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="news",
            name="author",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="news", name="downvotes", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="news",
            name="full_post_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="news",
            name="sentiment_feedback",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="news",
            name="source_page",
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="news", name="upvotes", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="news",
            name="url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
    ]