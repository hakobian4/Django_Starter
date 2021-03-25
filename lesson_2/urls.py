from django.urls import path
from lesson_2 import views

urlpatterns = [
    path('index/', views.index, name='index-view'),
    path('bio/<username>/', views.bio, name='bio'),
]
