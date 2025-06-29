# events/models.py
from django.contrib.auth.models import User
from django.db import models
from colorfield.fields import ColorField

# --- НАШ НОВЫЙ ЧЕРТЕЖ ДЛЯ ТИПОВ СОБЫТИЙ ---
class EventType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название типа")
    color = ColorField(default='#3788d8', verbose_name="Цвет")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип события"
        verbose_name_plural = "Типы событий"

class Teacher(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    bio = models.TextField(verbose_name="Краткая информация", blank=True)
    photo = models.ImageField(upload_to='teachers/', verbose_name="Фото", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

# --- НАШ ОБНОВЛЕННЫЙ ЧЕРТЕЖ СОБЫТИЯ ---
class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название события")
    description = models.TextField(verbose_name="Описание")
    date = models.DateField(verbose_name="Дата события")
    
    # --- НОВЫЕ ПОЛЯ ---
    start_time = models.TimeField(verbose_name="Время начала", null=True, blank=True)
    duration = models.PositiveIntegerField(verbose_name="Длительность в минутах", null=True, blank=True, help_text="Укажите длительность в минутах")
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тип события")

    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Преподаватель")

    participants = models.ManyToManyField(
        User,
        blank=True,
        verbose_name="Викладач",
        related_name="events_participated"
    )

    def __str__(self):
        return f"{self.date}: {self.title}"

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"