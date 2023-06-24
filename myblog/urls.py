from django.contrib import admin
from .views import Index,Profile, Detailed
from django.urls import path,include

urlpatterns = [
    path('',Index.as_view()),
    path('profile/',Profile.as_view()),
    path('detail/<int:pk>/', Detailed.as_view(), name='detail')
]
