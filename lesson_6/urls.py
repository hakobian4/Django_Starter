from django.urls import path
from lesson_6 import views


urlpatterns = [
    path('try-form/', views.my_form, name='my_form'),
    path('try-modelform/', views.ModelFormView.as_view(), name='modelform'),
    path('class-form/', views.MyFormView.as_view(), name='class_form'),
]