from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('<int:user_id>/', views.chat_view, name='chat'),
]
