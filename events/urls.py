# events/urls.py

from django.urls import path
from .views import event_list, event_type_list, event_detail

urlpatterns = [
    # Этот путь теперь соответствует /api/events/
    path('', event_list, name='event_list'),
    
    # Этот путь теперь соответствует /api/events/types/
    path('types/', event_type_list, name='event_type_list'),

    # Этот путь теперь соответствует /api/events/5/
    path('<int:event_id>/', event_detail, name='event_detail'),
]