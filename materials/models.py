from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    """
    Класс для описания модели курсов
    """
    title = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    description = models.TextField(
        verbose_name="Описание курса", **NULLABLE, help_text="Введите описание курса"
    )
    image = models.ImageField(
        upload_to="materials/course",
        verbose_name="Превью",
        **NULLABLE,
        help_text="Загрузите превью"
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """
    Класс для описания модели уроков
    """
    title = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока", **NULLABLE, help_text="Введите описание урока"
    )
    image = models.ImageField(
        upload_to="materials/lesson",
        verbose_name="Превью",
        **NULLABLE,
        help_text="Загрузите превью"
    )
    video_link = models.URLField(
        **NULLABLE,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", related_name="course"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
