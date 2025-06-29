# events/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Event, EventType

def event_type_list(request):
    """
    Отдает список всех типов событий для построения фильтра на фронтенде
    """
    types = EventType.objects.all()
    data = [{'id': type.id, 'name': type.name, 'color': type.color} for type in types]
    return JsonResponse(data, safe=False)

def event_list(request):
    """
    Отдает список событий. Может фильтровать по типам,
    если передан GET-параметр ?types=1,2,3
    """
    events = Event.objects.all().select_related('teacher', 'event_type') # Оптимизация запроса

    types_query = request.GET.get('types')
    if types_query:
        type_ids = [int(id) for id in types_query.split(',') if id.isdigit()]
        if type_ids:
            events = events.filter(event_type_id__in=type_ids)
    
    data = []
    for event in events:
        # --- Блок для подготовки данных о преподавателе ---
        teacher_data = None
        if event.teacher:
            teacher_data = {
                'full_name': event.teacher.full_name,
                'bio': event.teacher.bio,
                'photo_url': request.build_absolute_uri(event.teacher.photo.url) if event.teacher.photo else None
            }
        # --- Конец блока ---

        data.append({
            'id': event.id, 
            'title': event.title,
            'start': event.date.strftime("%Y-%m-%d"),
            'color': event.event_type.color if event.event_type else '#3788d8',
            'description': event.description,
            'start_time': event.start_time.strftime("%H:%M") if event.start_time else None,
            'duration': event.duration,
            'event_type': event.event_type.name if event.event_type else None,
            'teacher': teacher_data # Добавляем данные о преподавателе
        })
    return JsonResponse(data, safe=False)

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    teacher_data = None
    if event.teacher:
        teacher_data = {
            'full_name': event.teacher.full_name,
            'bio': event.teacher.bio,
            # Формируем полный URL для фото
            'photo_url': request.build_absolute_uri(event.teacher.photo.url) if event.teacher.photo else None
        }
    
    participants_data = []
    for user in event.participants.all():
        participants_data.append({
            'id': user.id,
            'full_name': user.get_full_name() or user.username
        })

    data = {
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'date': event.date.strftime("%Y-%m-%d"),
        'start_time': event.start_time.strftime("%H:%M") if event.start_time else None,
        'duration': event.duration,
        'event_type': event.event_type.name if event.event_type else None,
        # --- И СЮДА ТОЖЕ ---
        'color': event.event_type.color if event.event_type else '#3788d8',
        'teacher': teacher_data,
        'participants': participants_data
    }
    return JsonResponse(data)

# View для главной страницы (без изменений)
def calendar_view(request):
    return render(request, 'events/calendar.html')