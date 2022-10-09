from django.contrib import admin
from django.urls import path
from contact.views import emailView, Follow

urlpatterns = [
    path('ulasin', emailView, name='ulasin'),
    path("takip", Follow, name="takip"),
]
