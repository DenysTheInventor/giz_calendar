# events/models.py

from django.db import models

# --- НАШ НОВЫЙ ЧЕРТЕЖ ДЛЯ ТИПОВ СОБЫТИЙ ---
class EventType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название типа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип события"
        verbose_name_plural = "Типы событий"


# --- НАШ ОБНОВЛЕННЫЙ ЧЕРТЕЖ СОБЫТИЯ ---
class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название события")
    description = models.TextField(verbose_name="Описание")
    date = models.DateField(verbose_name="Дата события")
    
    # --- НОВЫЕ ПОЛЯ ---
    start_time = models.TimeField(verbose_name="Время начала", null=True, blank=True)
    duration = models.PositiveIntegerField(verbose_name="Длительность в минутах", null=True, blank=True, help_text="Укажите длительность в минутах")
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тип события")

    def __str__(self):
        return f"{self.date}: {self.title}"

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"