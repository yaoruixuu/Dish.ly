from django.urls import path
from . import views

urlpatterns = [
     

     #chatbot
     path("", views.chat_view, name="chat_view")
 ]