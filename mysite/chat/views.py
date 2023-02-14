from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

#
# def chatPage(request, *args, **kwargs):
#     if not request.user.is_authenticated:
#         return redirect("login-user")
#     context = {}
#     return render(request, "chat/chatPage.html", context)
