from django.shortcuts import render


def index(request):
    return render(request, 'pardy/index.html', {})

def room(request, room_name):
    return render(request, 'pardy/room.html', {
        'room_name': room_name
    })