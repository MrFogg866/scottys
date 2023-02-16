from django.shortcuts import render
from .models import Event

def event_book(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'event/event_book.html', context)

