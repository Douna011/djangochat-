from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from .utils import get_or_create_room

# @login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)  # Don't show yourself
    return render(request, 'chat/user_list.html', {'users': users})

# @login_required
def chat_view(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    room = get_or_create_room(request.user, other_user)

    if request.method == "POST":
        msg = request.POST.get("message")
        if msg:
            Message.objects.create(
                room=room,
                sender=request.user,
                text=msg
            )
        return redirect('chat', user_id=other_user.id)

    messages = room.messages.order_by("created_at")
    return render(request, "chat/chat.html", {
    "room": room,
    "messages": messages,
    "other_user": other_user
})

