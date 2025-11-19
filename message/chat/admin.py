from django.contrib import admin
from .models import ChatRoom, Message


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'user1', 'user2')
    search_fields = ('user1__username', 'user2__username')
    list_filter = ('user1', 'user2')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'sender', 'text', 'created_at')
    search_fields = ('sender__username', 'text')
    list_filter = ('sender', 'created_at')
    ordering = ('-created_at',)
