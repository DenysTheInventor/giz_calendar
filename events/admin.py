# events/admin.py
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Event, EventType, Teacher

# Создаем класс для кастомизации админки EventType
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'color') # Показываем имя и цвет в списке
    search_fields = ('name',) # Добавляем поиск по имени

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'event_type', 'teacher')
    list_filter = ('date', 'event_type', 'teacher')
    search_fields = ('title', 'description')
    # Улучшенный виджет для выбора пользователей
    filter_horizontal = ('participants',)

    # Эта функция заставляет поле 'participants' показывать только пользователей из группы 'Teachers'
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "participants":
            kwargs["queryset"] = User.objects.filter(groups__name='Teachers')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Event)
admin.site.register(EventType, EventTypeAdmin) # Регистрируем модель с кастомизацией
admin.site.register(Teacher)