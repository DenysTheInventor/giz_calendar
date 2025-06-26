# events/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Event

# Обновляем список событий
def event_list(request):
    events = Event.objects.all()
    data = []
    for event in events:
        data.append({
            'id': event.id, 
            'title': event.title,
            'start': event.date.strftime("%Y-%m-%d"),
            # Добавляем новые поля в JSON
            'description': event.description,
            'start_time': event.start_time.strftime("%H:%M") if event.start_time else None,
            'duration': event.duration,
            'event_type': event.event_type.name if event.event_type else None,
        })
    return JsonResponse(data, safe=False)

# Обновляем одно событие
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    data = {
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'date': event.date.strftime("%Y-%m-%d"),
        # И сюда тоже добавляем новые поля
        'start_time': event.start_time.strftime("%H:%M") if event.start_time else None,
        'duration': event.duration,
        'event_type': event.event_type.name if event.event_type else None,
    }
    return JsonResponse(data)

# View для главной страницы (без изменений)
def calendar_view(request):
    return render(request, 'events/calendar.html')