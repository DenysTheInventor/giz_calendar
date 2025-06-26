# events/urls.py

from django.urls import path
from .views import event_list, event_detail # <-- импортируем event_detail

urlpatterns = [
    # /api/events/
    path('', event_list, name='event_list'),
    # /api/events/5/
    path('<int:event_id>/', event_detail, name='event_detail'), # <-- НАШ НОВЫЙ URL
]