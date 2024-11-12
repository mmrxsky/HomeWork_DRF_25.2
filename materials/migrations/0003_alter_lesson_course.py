# Generated by Django 5.1.3 on 2024-11-12 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_alter_lesson_video_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lesson_count",
                to="materials.course",
                verbose_name="Курс",
            ),
        ),
    ]
