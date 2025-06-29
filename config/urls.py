# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Импортируем наш view для главной страницы календаря
from events.views import calendar_view

urlpatterns = [
    # Главная страница ('/') теперь четко ведет на view календаря.
    path('', calendar_view, name='home'),

    # Админка
    path('admin/', admin.site.urls),
    
    # Все API-запросы к событиям сгруппированы под префиксом /api/events/
    # и передаются в файл events.urls
    path('api/events/', include('events.urls')),
]

# Обслуживание медиа-файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)