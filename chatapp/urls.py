from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat_view'),
    path('api/chatbot/', views.chatbot_api, name='chatbot_api'),
]
