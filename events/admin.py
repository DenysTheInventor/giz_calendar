# events/admin.py

from django.contrib import admin
from .models import Event, EventType # <-- Добавляем импорт EventType

# Register your models here.
admin.site.register(Event)
admin.site.register(EventType) # <-- Регистрируем новую модель